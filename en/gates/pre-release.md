# Pre-release Gate

- **Gate ID**: `GATE-PRE-RELEASE`
- **Actor**: Release owner; an agent may perform checks, but publication remains authorized
- **Evidence**: Scope, version, validation, Git state, release notes, and artifact checks
- **Blocking**: Yes; artifact, version, secret, validation, or authorization failures block release

- [ ] Release scope and version are determined (`REL-001`, `REL-002`).
- [ ] Applicable validation and regression checks were run.
- [ ] README, docs, examples, and release notes match the contents (`DOC-001`, `REL-006`).
- [ ] Artifact was created and reopened or extracted for verification (`REL-004`).
- [ ] No secrets, runtime data, debug dumps, or cache are included.
- [ ] Unverified platforms or services are clearly marked (`CORE-010`).
- [ ] Tag or publication has applicable authorization (`REL-007`).
