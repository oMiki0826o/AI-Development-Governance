# Pre-push Gate

- **Gate ID**: `GATE-PRE-PUSH`
- **Actor**: Agent or developer preparing a push
- **Evidence**: Branch, remote, upstream, commits, working-tree state, and validation results
- **Blocking**: Yes; unclear remote, secrets, or unauthorized history rewrite block push

- [ ] Branch and remote are correct.
- [ ] The commits intended for push were reviewed.
- [ ] The working tree and applicable validation are known.
- [ ] No secrets or local data are included.
- [ ] Force push or history rewrite has explicit `DEC-004` authorization (`GIT-005`).
