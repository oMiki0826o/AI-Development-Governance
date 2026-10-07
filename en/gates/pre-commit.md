# Pre-commit Gate

- **Gate ID**: `GATE-PRE-COMMIT`
- **Actor**: Agent or developer preparing a commit
- **Evidence**: Status, diffs, staged diff, validation commands, and results
- **Blocking**: Yes; unclear scope, secrets, or failed required validation block commit

- [ ] `git status` and `git diff` were reviewed (`GIT-001`).
- [ ] Staged files form a coherent work unit (`GIT-002`).
- [ ] No secrets, runtime data, logs, cache, or unintended artifacts are staged.
- [ ] Applicable syntax, parse, test, or lint checks were run (`VAL-010`).
- [ ] Regression risk and documentation synchronization were reviewed (`VAL-008`, `DOC-002`).
