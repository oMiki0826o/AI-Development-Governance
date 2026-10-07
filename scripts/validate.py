#!/usr/bin/env python3
"""
scripts/validate.py

Modification():
- Validate repository structure, text encoding, links, rule IDs, gate metadata, and version consistency.

Responsibility:
Provide deterministic checks for objective repository invariants without attempting to judge policy quality.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
TEXT_SUFFIXES = {'.md', '.py', '.yml', '.yaml', '.json', '.toml', '.txt'}
COMMON_REQUIRED_FILES = {
    'README.md', 'QUICKSTART.md', 'CHANGELOG.md', 'LICENSE', 'VERSION',
    'AGENTS.md', 'DEPENDENCIES.md',
}
LANGUAGES = ('zh-TW', 'en')
LANGUAGE_REQUIRED_DIRS = ('rules', 'workflows', 'gates', 'templates', 'docs')
LANGUAGE_REQUIRED_FILES = (
    'rules/core.md', 'rules/decision.md', 'rules/convergence.md',
    'rules/project-bootstrap.md', 'rules/file-format.md', 'rules/engineering.md',
    'rules/validation.md', 'rules/documentation.md', 'rules/git.md', 'rules/release.md',
    'workflows/task-lifecycle.md', 'workflows/bugfix.md', 'workflows/release.md',
    'gates/pre-edit.md', 'gates/pre-commit.md', 'gates/pre-push.md', 'gates/pre-release.md',
    'templates/GithubRepoTemplate.md',
)
RULE_HEADING_RE = re.compile(r'^###\s+((?:CORE|DEC|CONV|BOOT|FMT|ENG|VAL|DOC|GIT|REL)-\d{3})\b', re.MULTILINE)
MD_LINK_RE = re.compile(r'(?<!!)\[[^\]]*\]\(([^)]+)\)')
SEMVER_RE = re.compile(r'^\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?$')


def text_files() -> list[Path]:
    result: list[Path] = []
    for path in ROOT.rglob('*'):
        if not path.is_file():
            continue
        if '.git' in path.parts:
            continue
        if path.name in {'LICENSE', 'VERSION'} or path.suffix.lower() in TEXT_SUFFIXES:
            result.append(path)
    return sorted(result)


def check_required(errors: list[str]) -> None:
    for rel in sorted(COMMON_REQUIRED_FILES):
        if not (ROOT / rel).is_file():
            errors.append(f'missing required file: {rel}')
    for language in LANGUAGES:
        for directory in LANGUAGE_REQUIRED_DIRS:
            if not (ROOT / language / directory).is_dir():
                errors.append(f'missing language directory: {language}/{directory}')
        for rel in LANGUAGE_REQUIRED_FILES:
            if not (ROOT / language / rel).is_file():
                errors.append(f'missing required file: {language}/{rel}')


def read_utf8(path: Path, errors: list[str]) -> str | None:
    raw = path.read_bytes()
    try:
        text = raw.decode('utf-8')
    except UnicodeDecodeError as exc:
        errors.append(f'{path.relative_to(ROOT)}: not valid UTF-8 ({exc})')
        return None
    if b'\r' in raw:
        errors.append(f'{path.relative_to(ROOT)}: contains CR/CRLF; expected LF')
    if raw and not raw.endswith(b'\n'):
        errors.append(f'{path.relative_to(ROOT)}: missing final newline')
    return text


def check_markdown_links(path: Path, text: str, errors: list[str]) -> None:
    # Example links inside fenced code blocks are templates, not repository links.
    scan_text = re.sub(r'```.*?```', '', text, flags=re.DOTALL)
    for match in MD_LINK_RE.finditer(scan_text):
        target = match.group(1).strip()
        if not target or target.startswith(('#', 'http://', 'https://', 'mailto:')):
            continue
        target = target.split('#', 1)[0].strip()
        if target.startswith('<') and target.endswith('>'):
            target = target[1:-1]
        target = unquote(target)
        if not target:
            continue
        resolved = (path.parent / target).resolve()
        try:
            resolved.relative_to(ROOT.resolve())
        except ValueError:
            errors.append(f'{path.relative_to(ROOT)}: relative link escapes repository: {target}')
            continue
        if not resolved.exists():
            errors.append(f'{path.relative_to(ROOT)}: broken relative link: {target}')


def check_rule_ids(errors: list[str]) -> None:
    language_ids: dict[str, set[str]] = {}
    for language in LANGUAGES:
        seen: dict[str, Path] = {}
        for path in sorted((ROOT / language / 'rules').glob('*.md')):
            text = path.read_text(encoding='utf-8')
            ids = RULE_HEADING_RE.findall(text)
            if not ids:
                errors.append(f'{path.relative_to(ROOT)}: no Rule ID found')
            for rule_id in ids:
                if rule_id in seen:
                    errors.append(
                        f'duplicate Rule ID {rule_id}: '
                        f'{seen[rule_id].relative_to(ROOT)} and {path.relative_to(ROOT)}'
                    )
                else:
                    seen[rule_id] = path
        language_ids[language] = set(seen)
    if language_ids.get('zh-TW') != language_ids.get('en'):
        errors.append('zh-TW and en Rule ID sets do not match')


def check_gates(errors: list[str]) -> None:
    required_markers = ['**Gate ID**:', '**Actor**:', '**Evidence**:', '**Blocking**:']
    language_gate_ids: dict[str, set[str]] = {}
    for language in LANGUAGES:
        gate_ids: set[str] = set()
        for path in sorted((ROOT / language / 'gates').glob('*.md')):
            text = path.read_text(encoding='utf-8')
            for marker in required_markers:
                if marker not in text:
                    errors.append(f'{path.relative_to(ROOT)}: missing gate metadata {marker}')
            match = re.search(r'\*\*Gate ID\*\*:\s*`([^`]+)`', text)
            if match:
                gate_id = match.group(1)
                if gate_id in gate_ids:
                    errors.append(f'duplicate Gate ID: {gate_id} in {language}')
                gate_ids.add(gate_id)
        language_gate_ids[language] = gate_ids
    if language_gate_ids.get('zh-TW') != language_gate_ids.get('en'):
        errors.append('zh-TW and en Gate ID sets do not match')


def check_version(errors: list[str]) -> None:
    version = (ROOT / 'VERSION').read_text(encoding='utf-8').strip()
    if not SEMVER_RE.fullmatch(version):
        errors.append(f'VERSION is not basic SemVer: {version!r}')
        return

    readme = (ROOT / 'README.md').read_text(encoding='utf-8')
    if f'version-{version}-blue' not in readme:
        errors.append('README version badge does not match VERSION')

    changelog = (ROOT / 'CHANGELOG.md').read_text(encoding='utf-8')
    first_version = re.search(r'^##\s+([^\s]+)', changelog, flags=re.MULTILINE)
    if not first_version or first_version.group(1) != version:
        errors.append('latest CHANGELOG version does not match VERSION')

    license_text = (ROOT / 'LICENSE').read_text(encoding='utf-8')
    if license_text.startswith('MIT License') and 'license-MIT-green' not in readme:
        errors.append('README license badge does not match MIT LICENSE')


def main() -> int:
    errors: list[str] = []
    check_required(errors)

    for path in text_files():
        text = read_utf8(path, errors)
        if text is not None and path.suffix.lower() == '.md':
            check_markdown_links(path, text, errors)

    check_rule_ids(errors)
    check_gates(errors)
    check_version(errors)

    if errors:
        print(f'Validation failed with {len(errors)} issue(s):')
        for error in errors:
            print(f'- {error}')
        return 1

    print('Validation passed.')
    print(f'- text files checked: {len(text_files())}')
    print(f'- version: {(ROOT / "VERSION").read_text(encoding="utf-8").strip()}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
