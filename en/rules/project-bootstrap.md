# Project Bootstrap Policy

### BOOT-001 — Minimum project content

A project should provide a README, LICENSE, `.gitignore`, dependency definition or an explicit no-dependency statement, project content, and a `data/` separation.

### BOOT-002 — Dependencies must be traceable

Use one appropriate dependency definition. Do not create an empty manifest merely for appearance.

### BOOT-003 — Separate runtime and AI work data

Use `data/runtime/` for runtime output and `data/ai/` for project context, decisions, plans, handoff material, and collaboration records. The entire `data/` directory is local and ignored by default.

### BOOT-004 — Create directories conditionally

Create tests, docs, scripts, config, source, and CI directories only when they have a real purpose.

### BOOT-005 — Bootstrap must be usable

Before completion, the README, license, ignore rules, dependencies, entry point, and installation or startup state must be clear and accurate.
