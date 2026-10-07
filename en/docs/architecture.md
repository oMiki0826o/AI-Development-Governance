# Architecture

The repository separates Rules, Workflows, Gates, Templates, Docs, and Tooling by responsibility.

- `rules/` contains authoritative governance rules.
- `workflows/` sequences existing rules.
- `gates/` provides stage checks and evidence requirements.
- `templates/` defines reusable output formats.
- `docs/` explains usage and background for human readers.
- Root `scripts/` performs objective checks only.
