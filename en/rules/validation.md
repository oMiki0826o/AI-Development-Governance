# Validation Policy

### VAL-001 — Level 0: Inspection

Reading code, diffs, configuration, and documentation supports analysis but not a claim of runtime verification.

### VAL-002 — Level 1: Syntax / Parse / Compile

This proves only that the relevant parser or compiler accepts the content.

### VAL-003 — Level 2: Static analysis

Run applicable linters, type checks, or static analyzers and report their actual scope.

### VAL-004 — Level 3: Unit tests

Run relevant isolated tests and report the tested behavior.

### VAL-005 — Level 4: Integration tests

Verify interactions between real components where applicable.

### VAL-006 — Level 5: Smoke test

Verify the smallest meaningful end-to-end path.

### VAL-007 — Level 6: Real environment verification

Only real execution in the required environment supports a full environment claim.

### VAL-008 — Regression must cover affected paths

Review existing behavior and relevant old paths after a change.

### VAL-009 — Do not break tests for a green result

Fix implementation or requirements; do not weaken tests merely to pass.

### VAL-010 — Report precisely

State commands run, results, validation level, and unverified limitations.
