# Pre-edit Gate

- **Gate ID**: `GATE-PRE-EDIT`
- **Actor**: Agent or developer performing the change
- **Evidence**: Relevant files read, requirements understood, and required decisions recorded
- **Blocking**: Yes; unresolved high-risk unknowns or possible data loss block editing

- [ ] Requirements and completion conditions are understood (`CORE-001`).
- [ ] Relevant architecture, entry points, callers, callees, configuration, and tests were read (`ENG-001`).
- [ ] Facts, inferences, and unverified items are separated (`CORE-002`, `CORE-003`).
- [ ] Scope excludes unrelated refactoring (`CORE-005`).
- [ ] Required decisions and authorization were handled (`DEC-003`, `DEC-004`).
- [ ] Existing unconfirmed work will not be overwritten (`CORE-007`).
