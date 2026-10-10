#!/usr/bin/env python3
"""
scripts/validate.py

Modification():
- 1.2.0: Report missing/corrupt files without crashing; validate rule and gate
  references, Markdown targets/anchors, language parity and SemVer.
"""

from __future__ import annotations

import argparse
import re
import unicodedata
from pathlib import Path
from urllib.parse import unquote, urlsplit

LANGUAGES = ('zh-TW', 'en')
LANG_DIRS = ('rules', 'workflows', 'gates', 'templates', 'docs')
REQUIRED = ('README.md', 'QUICKSTART.md', 'AGENTS.md', 'LICENSE',
            'VERSION', 'CHANGELOG.md', 'DEPENDENCIES.md', '.gitignore',
            'scripts/bootstrap_project.py', 'scripts/validate.py',
            '.github/workflows/validate.yml')
REQUIRED_LANG = ('rules/core.md', 'rules/decision.md', 'rules/convergence.md',
                 'rules/project-bootstrap.md', 'rules/file-format.md',
                 'rules/engineering.md', 'rules/validation.md',
                 'rules/documentation.md', 'rules/git.md', 'rules/release.md',
                 'workflows/task-lifecycle.md', 'workflows/bugfix.md',
                 'workflows/release.md', 'gates/pre-edit.md', 'gates/pre-commit.md',
                 'gates/pre-push.md', 'gates/pre-release.md',
                 'templates/GithubRepoTemplate.md', 'templates/project-agents.md',
                 'templates/project-memory.md', 'templates/work-record.md')
RULE_ID = re.compile(r'\b(?:CORE|DEC|CONV|BOOT|FMT|ENG|VAL|DOC|GIT|REL)-\d{3}\b')
HEADING_ID = re.compile(r'^###\s+((?:CORE|DEC|CONV|BOOT|FMT|ENG|VAL|DOC|GIT|REL)-\d{3})\b', re.M)
GATE_ID = re.compile(r'^GATE-[A-Z0-9]+(?:-[A-Z0-9]+)*$')
SEMVER = re.compile(r'^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)'
                    r'(?:-((?:0|[1-9]\d*|[0-9A-Za-z-]*[A-Za-z-][0-9A-Za-z-]*)'
                    r'(?:\.(?:0|[1-9]\d*|[0-9A-Za-z-]*[A-Za-z-][0-9A-Za-z-]*))*))?'
                    r'(?:\+([0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*))?$')
TEXT_SUFFIXES = {'.md', '.py', '.yml', '.yaml', '.json', '.toml', '.txt', '.ini'}
SKIP = {'.git', '.venv', 'venv', '__pycache__', 'data', 'node_modules',
        '.pytest_cache', '.mypy_cache', '.ruff_cache', '.tox', '.idea'}


class Validator:
    def __init__(self, root: Path):
        self.root = root.resolve()
        self.errors: list[str] = []
        self.contents: dict[Path, str] = {}

    def fail(self, text: str) -> None:
        self.errors.append(text)

    def relative(self, path: Path) -> str:
        return path.relative_to(self.root).as_posix()

    def get(self, path: str | Path) -> str | None:
        file = self.root / path if isinstance(path, str) else path
        if file in self.contents:
            return self.contents[file]
        if file.is_symlink():
            self.fail(f'{self.relative(file)}: symlink source is not supported')
            return None
        if not file.is_file():
            self.fail(f'missing required file: {self.relative(file)}')
            return None
        try:
            raw = file.read_bytes()
        except OSError as exc:
            self.fail(f'{self.relative(file)}: cannot read: {exc}')
            return None
        try:
            data = raw.decode('utf-8')
        except UnicodeDecodeError as exc:
            self.fail(f'{self.relative(file)}: invalid UTF-8: {exc}')
            return None
        if raw.startswith(b'\xef\xbb\xbf'):
            self.fail(f'{self.relative(file)}: unexpected UTF-8 BOM')
        if b'\r' in raw:
            self.fail(f'{self.relative(file)}: CR/CRLF detected; use LF')
        if raw and not raw.endswith(b'\n'):
            self.fail(f'{self.relative(file)}: missing trailing LF')
        for n, line in enumerate(data.splitlines(), 1):
            if line.rstrip(' \t') != line:
                self.fail(f'{self.relative(file)}:{n}: trailing whitespace')
        self.contents[file] = data
        return data

    def walk_files(self) -> list[Path]:
        """Do not follow symlinks or inspect local runtime data."""
        import os
        collected: list[Path] = []
        for parent, dirs, files in os.walk(self.root, followlinks=False):
            dirs[:] = sorted(d for d in dirs if d not in SKIP and not (Path(parent) / d).is_symlink())
            for name in sorted(files):
                path = Path(parent) / name
                if path.is_symlink():
                    self.fail(f'{self.relative(path)}: symlink must be reviewed')
                    continue
                if path.suffix.lower() in TEXT_SUFFIXES or name in {'VERSION', 'LICENSE', '.gitignore'}:
                    collected.append(path)
        return collected

    def check_required(self) -> None:
        for name in REQUIRED:
            if not (self.root / name).is_file():
                self.fail(f'missing required file: {name}')
        for lang in LANGUAGES:
            for directory in LANG_DIRS:
                if not (self.root / lang / directory).is_dir():
                    self.fail(f'missing language directory: {lang}/{directory}')
            for path in REQUIRED_LANG:
                if not (self.root / lang / path).is_file():
                    self.fail(f'missing required file: {lang}/{path}')

    @staticmethod
    def strip_code(text: str) -> str:
        lines = []
        fenced = False
        fence_char = ''
        fence_count = 0
        for line in text.splitlines():
            start = re.match(r'^\s{0,3}(`{3,}|~{3,})', line)
            if start:
                chars = start.group(1)
                if not fenced:
                    fenced = True
                    fence_char, fence_count = chars[0], len(chars)
                    lines.append('')
                    continue
                if chars[0] == fence_char and len(chars) >= fence_count:
                    fenced = False
                    lines.append('')
                    continue
            lines.append('' if fenced else line)
        return '\n'.join(lines)

    @staticmethod
    def slugs(text: str) -> set[str]:
        slugs: set[str] = set()
        duplicates: dict[str, int] = {}
        for line in text.splitlines():
            m = re.match(r'^\s{0,3}#{1,6}\s+(.+?)\s*#*\s*$', line)
            if not m:
                continue
            title = re.sub(r'<[^>]*>|\[([^\]]+)\]\([^)]*\)|[`*_~]', '', m.group(1))
            title = title.lower().strip()
            title = ''.join(ch for ch in title if ch in '-_ ' or ch.isalnum() or unicodedata.category(ch).startswith('L'))
            base = re.sub(r'\s+', '-', title)
            n = duplicates.get(base, 0)
            duplicates[base] = n + 1
            slugs.add(f'{base}-{n}' if n else base)
        for m in re.finditer(r'<(?:a|span)\s+(?:name|id)=["\']([^"\']+)["\']', text):
            slugs.add(m.group(1))
        return slugs

    @staticmethod
    def link_targets(text: str) -> list[str]:
        """Find inline and reference targets; supports one or more nested parentheses."""
        targets: list[str] = []
        # Reference definitions, including image reference definitions.
        refs: dict[str, str] = {}
        for match in re.finditer(r'^\s{0,3}\[([^\]]+)\]:\s*(<[^>]*>|\S+)', text, re.M):
            refs[match.group(1).casefold()] = match.group(2).strip('<>')
            targets.append(match.group(2).strip('<>'))
        pos = 0
        while pos < len(text):
            left = text.find('[', pos)
            if left < 0:
                break
            right = text.find(']', left + 1)
            if right < 0:
                break
            i = right + 1
            if i < len(text) and text[i] == '(':
                depth, j, escaped = 1, i + 1, False
                while j < len(text) and depth:
                    c = text[j]
                    if escaped:
                        escaped = False
                    elif c == '\\':
                        escaped = True
                    elif c == '(':
                        depth += 1
                    elif c == ')':
                        depth -= 1
                    j += 1
                if depth == 0:
                    dest = text[i+1:j-1].strip()
                    if dest.startswith('<'):
                        dest = dest[1:].split('>', 1)[0]
                    else:
                        dest = re.split(r'\s+["\']', dest, maxsplit=1)[0]
                    targets.append(dest)
                    pos = j
                    continue
            elif i < len(text) and text[i] == '[':
                ending = text.find(']', i + 1)
                if ending > 0:
                    key = text[i + 1:ending].casefold() or text[left+1:right].casefold()
                    if key in refs:
                        # Already examined the reference definition.
                        pass
                    else:
                        targets.append(f'!missing-reference:{key}')
                    pos = ending + 1
                    continue
            pos = right + 1
        return targets

    def check_markdown_links(self, path: Path, content: str) -> None:
        scan = self.strip_code(content)
        for dest in self.link_targets(scan):
            if dest.startswith('!missing-reference:'):
                self.fail(f'{self.relative(path)}: missing Markdown reference: {dest[19:]}')
                continue
            if not dest or dest.startswith(('http:', 'https:', 'mailto:', 'data:', '//')):
                continue
            if re.match(r'^[A-Za-z][A-Za-z0-9+.-]*:', dest):
                continue
            p = urlsplit(dest)
            name, anchor = unquote(p.path), unquote(p.fragment)
            resolved = path.parent / name if name else path
            # Do not let a link traverse outside the repository.
            try:
                resolved = resolved.resolve()
                resolved.relative_to(self.root)
            except ValueError:
                self.fail(f'{self.relative(path)}: link escapes repository: {dest}')
                continue
            if not resolved.exists():
                self.fail(f'{self.relative(path)}: broken link: {dest}')
                continue
            if anchor and resolved.is_file() and resolved.suffix == '.md':
                linked = self.get(resolved)
                if linked is not None and anchor not in self.slugs(self.strip_code(linked)):
                    self.fail(f'{self.relative(path)}: broken anchor: {dest}')

    def check_rule_ids(self) -> None:
        by_language: dict[str, set[str]] = {}
        for lang in LANGUAGES:
            seen: dict[str, str] = {}
            for file in sorted((self.root / lang / 'rules').glob('*.md')):
                content = self.get(file)
                if content is None:
                    continue
                headings = HEADING_ID.findall(content)
                if not headings:
                    self.fail(f'{self.relative(file)}: no rule heading ID')
                for rule in headings:
                    if rule in seen:
                        self.fail(f'duplicate {lang} rule ID {rule}: {seen[rule]} and {self.relative(file)}')
                    seen[rule] = self.relative(file)
            by_language[lang] = set(seen)
            for file in sorted((self.root / lang).rglob('*.md')):
                if not file.is_file():
                    continue
                content = self.get(file)
                if content is None:
                    continue
                for rule in set(RULE_ID.findall(self.strip_code(content))):
                    if rule not in seen:
                        self.fail(f'{self.relative(file)}: unknown Rule ID: {rule}')
        if by_language.get('zh-TW') != by_language.get('en'):
            self.fail('zh-TW and en have different Rule ID sets')

    def check_gates(self) -> None:
        language_ids: dict[str, set[str]] = {}
        for lang in LANGUAGES:
            seen: set[str] = set()
            for file in sorted((self.root / lang / 'gates').glob('*.md')):
                content = self.get(file)
                if content is None:
                    continue
                entries: dict[str, str] = {}
                for key in ('Gate ID', 'Actor', 'Evidence', 'Blocking'):
                    match = re.search(r'^\s*-\s*\*\*' + re.escape(key) + r'\*\*:[ \t]*(.*?)[ \t]*$', content, re.M)
                    if not match or not match.group(1):
                        self.fail(f'{self.relative(file)}: empty/missing Gate metadata: {key}')
                        continue
                    entries[key] = match.group(1).strip('` ')
                gid = entries.get('Gate ID', '')
                if gid and not GATE_ID.fullmatch(gid):
                    self.fail(f'{self.relative(file)}: malformed Gate ID {gid}')
                if gid in seen:
                    self.fail(f'{self.relative(file)}: duplicate Gate ID: {gid}')
                if gid:
                    seen.add(gid)
                if entries.get('Blocking', '').split('。', 1)[0].split(';', 1)[0].lower() not in ('yes', 'no', '是', '否'):
                    self.fail(f'{self.relative(file)}: Blocking must start with yes/no/是/否')
            language_ids[lang] = seen
        if language_ids.get('zh-TW') != language_ids.get('en'):
            self.fail('zh-TW and en have different Gate ID sets')

    def check_version(self) -> None:
        text = self.get('VERSION')
        if text is None:
            return
        version = text.strip()
        if not SEMVER.fullmatch(version):
            self.fail(f'VERSION: invalid SemVer: {version!r}')
            return
        readme = self.get('README.md')
        if readme is not None and f'version-{version}-' not in readme:
            self.fail('README version badge does not match VERSION')
        changelog = self.get('CHANGELOG.md')
        if changelog is not None:
            headings = re.search(r'^##\s+([^\s]+)', changelog, re.M)
            if not headings or headings.group(1) != version:
                self.fail('latest CHANGELOG version does not match VERSION')
        license_text = self.get('LICENSE')
        if readme is not None and license_text is not None:
            if license_text.startswith('MIT License') and 'license-MIT-' not in readme:
                self.fail('MIT license and README badge disagree')

    def check_ignore(self) -> None:
        data = self.get('.gitignore')
        if data is None:
            return
        lines = [line.strip() for line in data.splitlines()
                 if line.strip() and not line.lstrip().startswith('#')]
        if 'data/' not in lines and '/data/' not in lines:
            self.fail('.gitignore must contain data/')
        if any(line.startswith('!data/') or line == '!data' for line in lines):
            self.fail('.gitignore must not unignore local data')

    def check_bilingual_files(self) -> None:
        paths = []
        for lang in LANGUAGES:
            current = {p.relative_to(self.root / lang).as_posix()
                       for p in (self.root / lang).rglob('*.md') if p.is_file()}
            paths.append(current)
        if len(paths) == 2 and paths[0] != paths[1]:
            left, right = paths
            self.fail(f'language file mismatch; zh-TW only={sorted(left-right)}; en only={sorted(right-left)}')

    def run(self) -> int:
        if not self.root.is_dir():
            print(f'[ERROR] root is not a directory: {self.root}')
            return 2
        self.check_required()
        files = self.walk_files()
        for file in files:
            content = self.get(file)
            if content is not None and file.suffix.lower() == '.md':
                self.check_markdown_links(file, content)
        self.check_rule_ids()
        self.check_gates()
        self.check_version()
        self.check_ignore()
        self.check_bilingual_files()
        if self.errors:
            print(f'Validation failed: {len(self.errors)} issue(s)')
            for error in sorted(set(self.errors)):
                print(f'[ERROR] {error}')
            return 1
        print(f'Validation passed: {len(files)} text files, two languages, rule and gate references')
        return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description='Validate a governance repository')
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    options = parser.parse_args(argv)
    return Validator(options.root).run()


if __name__ == '__main__':
    raise SystemExit(main())
