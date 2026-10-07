#!/usr/bin/env python3
"""
scripts/bootstrap_project.py

Modification():
- Bootstrap project-level governance files in minimal, standard, or full mode.

Responsibility:
Copy a safe, reviewable snapshot of governance entry files into another repository without overwriting existing files by default.
"""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

MINIMAL = {
    'templates/project-agents.md': 'AGENTS.md',
    'templates/project-memory.md': 'data/ai/project-memory.md',
    'templates/work-record.md': 'data/ai/work-record-template.md',
}

STANDARD_EXTRA = {
    'rules/core.md': '.governance/rules/core.md',
    'rules/decision.md': '.governance/rules/decision.md',
    'rules/convergence.md': '.governance/rules/convergence.md',
    'rules/engineering.md': '.governance/rules/engineering.md',
    'rules/file-format.md': '.governance/rules/file-format.md',
    'rules/validation.md': '.governance/rules/validation.md',
    'rules/git.md': '.governance/rules/git.md',
    'workflows/task-lifecycle.md': '.governance/workflows/task-lifecycle.md',
    'workflows/bugfix.md': '.governance/workflows/bugfix.md',
    'gates/pre-edit.md': '.governance/gates/pre-edit.md',
    'gates/pre-commit.md': '.governance/gates/pre-commit.md',
    'gates/pre-push.md': '.governance/gates/pre-push.md',
}

FULL_EXTRA_DIRS = ['rules', 'workflows', 'gates', 'templates/github']


def mapping_for_mode(mode: str, language: str) -> dict[str, str]:
    languages = ('zh-TW', 'en') if language == 'bilingual' else (language,)
    mapping: dict[str, str] = {}
    for selected in languages:
        prefix = '' if language != 'bilingual' or selected == 'zh-TW' else '.governance/en/'
        mapping.update({f'{selected}/{src}': f'{prefix}{dst}' for src, dst in MINIMAL.items()})
    if mode in {'standard', 'full'}:
        for selected in languages:
            mapping.update({f'{selected}/{src}': f'.governance/{selected}/{dst}' for src, dst in STANDARD_EXTRA.items()})
    if mode == 'full':
        for selected in languages:
            for dirname in FULL_EXTRA_DIRS:
                base = ROOT / selected / dirname
                for src in base.rglob('*'):
                    if src.is_file():
                        rel = src.relative_to(ROOT).as_posix()
                        mapping[rel] = f'.governance/{rel}'
            mapping[f'{selected}/templates/GithubRepoTemplate.md'] = f'.governance/{selected}/templates/GithubRepoTemplate.md'
    return mapping


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Bootstrap AI Development Governance into a project.')
    parser.add_argument('target', type=Path, help='Target project directory.')
    parser.add_argument('--mode', choices=['minimal', 'standard', 'full'], default='minimal')
    parser.add_argument('--language', choices=['zh-TW', 'en', 'bilingual'], default='zh-TW')
    parser.add_argument('--force', action='store_true', help='Overwrite files that already exist.')
    parser.add_argument('--dry-run', action='store_true', help='Show planned changes without writing files.')
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    target = args.target.expanduser().resolve()
    if not target.exists() or not target.is_dir():
        print(f'Error: target directory does not exist: {target}', file=sys.stderr)
        return 2

    mapping = mapping_for_mode(args.mode, args.language)
    conflicts: list[Path] = []
    planned: list[tuple[Path, Path]] = []

    for src_rel, dst_rel in sorted(mapping.items()):
        src = ROOT / src_rel
        dst = target / dst_rel
        if dst.exists() and not args.force:
            conflicts.append(dst)
        planned.append((src, dst))

    records_dir = target / 'data/ai/records'
    if records_dir.exists() and not records_dir.is_dir():
        conflicts.append(records_dir)

    if conflicts:
        print('No files were written because these targets already exist:')
        for path in conflicts:
            print(f'- {path}')
        print('Review them first. Use --force only when overwrite is intentional.')
        return 3

    print(f'Mode: {args.mode}')
    print(f'Language: {args.language}')
    for src, dst in planned:
        print(f'- {src.relative_to(ROOT)} -> {dst.relative_to(target)}')
    print(f'- create directory: {records_dir.relative_to(target)}/')

    if args.dry_run:
        print('Dry run only; no files written.')
        return 0

    for src, dst in planned:
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)

    records_dir.mkdir(parents=True, exist_ok=True)
    gitkeep = records_dir / '.gitkeep'
    if not gitkeep.exists():
        gitkeep.write_text('', encoding='utf-8')

    print('Bootstrap completed.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
