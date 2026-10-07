# Engineering Policy

### ENG-001 — Trace the relevant scope before editing

Read the relevant entry points, callers, callees, configuration, tests, and data flow.

### ENG-002 — Require a real reason for architecture changes

Do not refactor merely because another architecture looks cleaner.

### ENG-003 — Prefer correctness and simplicity

Prioritize correct behavior, maintainability, clarity, and the smallest reasonable design.

### ENG-004 — Extract hard-coded values only when needed

Extract values when they represent configuration, environment differences, secrets, or changing policy.

### ENG-005 — Handle errors at the appropriate level

Do not silently swallow exceptions or hide failures.

### ENG-006 — Separate configuration and secrets

Keep non-sensitive configuration separate from credentials and secret material.

### ENG-007 — Confirm new dependencies are necessary

Check whether existing capabilities are sufficient before adding a dependency.

### ENG-008 — Complete resource lifecycles

Open resources must have appropriate cleanup and failure handling.

### ENG-009 — Refactoring must not silently change behavior

Preserve external behavior unless the change is intentional, documented, and authorized.
