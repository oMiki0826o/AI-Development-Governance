# Repository Agent Instructions

This file governs maintenance of this governance repository itself. Higher-priority platform and safety requirements always apply.

## Authoritative policies

- Chinese source: `zh-TW/rules/`.
- English equivalent: `en/rules/`.
- `workflows/` sequence existing rules; `gates/` collect checks; `templates/` define output formats; `docs/` explain usage and should remain human-readable.
- `templates/GithubRepoTemplate.md` is the highest-authority GitHub publication entry point. For README, LICENSE, `.gitignore`, Discord release copy, or repository descriptions, follow it before the split templates under `templates/github/`.
- Markdown file names and Rule IDs should remain aligned between the language editions.

## Before editing

Read the relevant Rule documents, check existing work and preserve original scope. If creating or substantially rewriting a README, read `templates/GithubRepoTemplate.md` first. Update linked workflow, gate, template, and documentation entries whenever an authoritative rule changes. Keep all AI collaboration documents, plans, handoff material, and runtime work in ignored `data/`; public conclusions belong in `docs/`. Do not publish raw collaboration records.

## Required checks

```bash
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
python3 -m py_compile scripts/*.py
```

Report real commands run and limitations. Git push and release require the appropriate authorization.
