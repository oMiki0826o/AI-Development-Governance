#!/usr/bin/env python3
"""
scripts/bootstrap_project.py

Modification():
- 1.2.0: Deterministic bilingual file mapping, transactional installation,
  safe local-data handling, Git ignore enforcement, and source manifest.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LANGUAGES = ('zh-TW', 'en')
STANDARD_FILES = (
    'rules/core.md', 'rules/decision.md', 'rules/convergence.md',
    'rules/engineering.md', 'rules/file-format.md', 'rules/validation.md',
    'rules/git.md', 'workflows/task-lifecycle.md', 'workflows/bugfix.md',
    'gates/pre-edit.md', 'gates/pre-commit.md', 'gates/pre-push.md',
)
MINIMAL_FILES = ('rules/core.md', 'rules/decision.md', 'workflows/task-lifecycle.md')
LOCAL_DATA = {
    'templates/project-memory.md': 'data/ai/project-memory.md',
    'templates/work-record.md': 'data/ai/work-record-template.md',
}


def select_languages(language: str) -> tuple[str, ...]:
    return LANGUAGES if language == 'bilingual' else (language,)


def mapping_for_mode(mode: str, language: str) -> dict[str, str]:
    """Produce exactly one destination for each source, without duplicate roots."""
    mapping: dict[str, str] = {}
    for lang in select_languages(language):
        if mode == 'full':
            choices = [p.relative_to(ROOT / lang).as_posix()
                       for directory in ('rules', 'workflows', 'gates', 'templates', 'docs')
                       for p in sorted((ROOT / lang / directory).rglob('*')) if p.is_file()]
        else:
            choices = STANDARD_FILES if mode == 'standard' else MINIMAL_FILES
        for rel in choices:
            mapping[f'{lang}/{rel}'] = f'.governance/{lang}/{rel}'
    preferred = 'zh-TW' if language == 'bilingual' else language
    for src, dest in LOCAL_DATA.items():
        mapping[f'{preferred}/{src}'] = dest
    return mapping


def _inside(path: Path, root: Path) -> bool:
    return path == root or root in path.parents


def _safe_destination(root: Path, rel: str) -> Path:
    raw = root / rel
    if raw.is_symlink():
        raise ValueError(f'symlink destination is not allowed: {rel}')
    cursor = raw.parent
    while cursor != root:
        if cursor.is_symlink():
            raise ValueError(f'symlink parent is not allowed: {cursor}')
        cursor = cursor.parent
    if not _inside(raw.resolve(), root.resolve()):
        raise ValueError(f'destination escapes project: {rel}')
    if raw.exists() and not raw.is_file():
        raise ValueError(f'destination is not a regular file: {rel}')
    return raw


def _gitignore_content(path: Path) -> bytes:
    """Keep existing .gitignore bytes and append the policy only when absent."""
    if not path.exists():
        return b'# Local runtime and AI collaboration records\ndata/\n'
    raw = path.read_bytes()
    decoded = raw.decode('utf-8')
    entries = [line.strip() for line in decoded.splitlines() if line.strip() and not line.lstrip().startswith('#')]
    # A negation could override the ignore policy: reject instead of silently claiming safety.
    if any(line.startswith('!data/') or line == '!data' for line in entries):
        raise ValueError('.gitignore contains a data/ exception; review it manually')
    if 'data/' in entries or '/data/' in entries:
        return raw
    newline = b'\r\n' if b'\r\n' in raw else b'\n'
    suffix = b'' if not raw or raw.endswith(b'\n') else newline
    return raw + suffix + newline + b'# Local runtime and AI collaboration records' + newline + b'data/' + newline


def _agent_instructions(language: str, mode: str) -> bytes:
    languages = select_languages(language)
    primary = languages[0]
    policies = '\n'.join(
        f'- `{lang}`: `.governance/{lang}/rules/core.md`, '
        f'`.governance/{lang}/rules/decision.md`, '
        f'`.governance/{lang}/workflows/task-lifecycle.md`.'
        for lang in languages
    )
    extra = ('\n- For bug fixes, read the corresponding `workflows/bugfix.md` and '
             '`rules/convergence.md` when present.' if mode != 'minimal' else '')
    return (f'# Repository Agent Instructions\n\n'
            f'This project uses AI Development Governance, revision recorded in '
            f'`.governance/manifest.json`. Use the project’s own conventions '
            f'and higher-priority safety instructions first.\n\n'
            f'## Governance entry points\n\n{policies}{extra}\n\n'
            f'Default language: `{primary}`. Read only the rules relevant to the current task.\n\n'
            f'## Project-specific configuration\n\n'
            f'Document the project architecture, main entry points, and test commands '
            f'here. Avoid repeating shared governance rules.\n\n'
            f'## Validation and reporting\n\n'
            f'Report commands actually executed and their outcomes. '
            f'Do not claim tests or integration checks that were not performed.\n').encode('utf-8')


def _version() -> str:
    return (ROOT / 'VERSION').read_text(encoding='utf-8').strip()


def _commit_id() -> str | None:
    try:
        proc = subprocess.run(['git', '-C', str(ROOT), 'rev-parse', 'HEAD'],
                              check=True, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL,
                              text=True, timeout=3)
    except (OSError, subprocess.CalledProcessError, subprocess.TimeoutExpired):
        return None
    return proc.stdout.strip() or None


def prepare_plan(target: Path, mode: str, language: str, force: bool) -> tuple[dict[str, bytes], list[str]]:
    mappings = mapping_for_mode(mode, language)
    plan: dict[str, bytes] = {}
    preserved: list[str] = []
    for src_rel, dst_rel in sorted(mappings.items()):
        src = ROOT / src_rel
        if not src.is_file() or src.is_symlink():
            raise ValueError(f'missing or unsafe governance source: {src_rel}')
        dst = _safe_destination(target, dst_rel)
        if dst_rel.startswith('data/ai/') and dst.exists():
            # Work data belongs to the destination project, never to the installer.
            preserved.append(dst_rel)
            continue
        if dst.exists() and not force:
            raise FileExistsError(f'destination exists (use --force after review): {dst_rel}')
        plan[dst_rel] = src.read_bytes()

    for rel, content in {
        'AGENTS.md': _agent_instructions(language, mode),
        '.gitignore': _gitignore_content(_safe_destination(target, '.gitignore')),
    }.items():
        dst = _safe_destination(target, rel)
        if rel == '.gitignore' and dst.exists() and dst.read_bytes() == content:
            continue
        if rel == 'AGENTS.md' and dst.exists() and not force:
            raise FileExistsError('AGENTS.md already exists (use --force after review)')
        plan[rel] = content

    manifest = {
        'format_version': 1,
        'governance_version': _version(),
        'source_commit': _commit_id(),
        'language': language,
        'mode': mode,
        'managed_files': {path: hashlib.sha256(content).hexdigest()
                          for path, content in sorted(plan.items())
                          if path.startswith('.governance/')},
    }
    manifest_rel = '.governance/manifest.json'
    dst = _safe_destination(target, manifest_rel)
    if dst.exists() and not force:
        raise FileExistsError(f'{manifest_rel} already exists (use --force after review)')
    plan[manifest_rel] = (json.dumps(manifest, ensure_ascii=False, indent=2,
                                    sort_keys=True) + '\n').encode('utf-8')
    return plan, preserved


def apply_plan(target: Path, plan: dict[str, bytes]) -> None:
    """Rollback changed files if one of the writes fails; leave prior work untouched."""
    previous: dict[Path, bytes | None] = {}
    created_dirs: list[Path] = []
    try:
        for rel, content in sorted(plan.items()):
            dst = _safe_destination(target, rel)
            existing = dst.read_bytes() if dst.exists() else None
            if existing == content:
                continue
            previous[dst] = existing
            missing: list[Path] = []
            parent = dst.parent
            while parent != target and not parent.exists():
                missing.append(parent)
                parent = parent.parent
            for directory in reversed(missing):
                directory.mkdir()
                created_dirs.append(directory)
            fd, name = tempfile.mkstemp(prefix='.governance-', dir=str(dst.parent))
            try:
                with os.fdopen(fd, 'wb') as handle:
                    handle.write(content)
                    handle.flush()
                    os.fsync(handle.fileno())
                if existing is not None:
                    os.chmod(name, dst.stat().st_mode & 0o777)
                os.replace(name, dst)
            finally:
                if os.path.exists(name):
                    os.unlink(name)
    except Exception:
        for dst, content in reversed(list(previous.items())):
            if content is None:
                dst.unlink(missing_ok=True)
            else:
                dst.write_bytes(content)
        for directory in reversed(created_dirs):
            try:
                directory.rmdir()
            except OSError:
                pass
        raise


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description='Install AI Development Governance into a project')
    parser.add_argument('target', type=Path)
    parser.add_argument('--mode', choices=('minimal', 'standard', 'full'), default='minimal')
    parser.add_argument('--language', choices=(*LANGUAGES, 'bilingual'), default='zh-TW')
    parser.add_argument('--force', action='store_true')
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args(argv)
    target = args.target.expanduser().resolve()
    if not target.is_dir():
        print(f'[ERROR] target is not a directory: {target}', file=sys.stderr)
        return 2
    if target == ROOT or _inside(target, ROOT) or _inside(ROOT, target):
        print('[ERROR] target must be separate from the governance source', file=sys.stderr)
        return 2
    try:
        plan, preserved = prepare_plan(target, args.mode, args.language, args.force)
        print(f'Governance {_version()} | {args.mode} | {args.language}')
        for path in sorted(plan):
            current = target / path
            status = ('unchanged' if current.is_file() and current.read_bytes() == plan[path]
                      else 'replace' if current.is_file() else 'create')
            print(f'  {status}: {path}')
        for path in preserved:
            print(f'  preserve user data: {path}')
        if args.dry_run:
            print('Dry run: no files written')
            return 0
        apply_plan(target, plan)
    except (OSError, UnicodeError, ValueError) as exc:
        print(f'[ERROR] {exc}', file=sys.stderr)
        return 3
    print('Bootstrap completed')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
