# Git Policy

### GIT-001 — Inspect status and diff first

Before changing Git state, inspect status, branch, and relevant diffs.

### GIT-002 — Do not stage blindly

Review files before staging; staged files must represent a coherent work unit.

### GIT-003 — Read-only Git operations are generally safe

Status, diff, log, branch inspection, and remote inspection can normally be performed autonomously.

### GIT-004 — Understand working-tree impact

Understand the effect before using commands that change the working tree.

### GIT-005 — Destructive operations require authorization

Require explicit authorization for hard reset, clean, force push, history rewrite, deletion, or data loss.

### GIT-006 — Do not split commits for contribution counts

Commit boundaries should describe meaningful work.

### GIT-007 — Do not use default answers for pull, merge, or rebase

Inspect branch and remote state before selecting an integration strategy.

### GIT-008 — Prefer traceable rollback after publication

Published history should remain recoverable and auditable.
