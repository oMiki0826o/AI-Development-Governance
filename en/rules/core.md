# Core Governance

These principles apply across projects and define observable, verifiable engineering behavior.

### CORE-001 — Understand before changing

Understand the relevant architecture, data flow, constraints, and current state before editing.

### CORE-002 — Prefer evidence

Confirm facts from code, configuration, tests, documentation, or tools before treating them as facts.

### CORE-003 — Do not fabricate results

Do not claim a command, test, review, or verification was completed unless it actually was.

### CORE-004 — Fix root causes first

Prefer a minimal root-cause fix over accumulating workarounds.

### CORE-005 — Control scope

Keep unrelated refactoring and improvements outside the current task.

### CORE-006 — Avoid unnecessary layers

Add abstractions only when they reduce total complexity and have a stable responsibility.

### CORE-007 — Protect existing work

Do not overwrite, delete, or revert unconfirmed changes from users or other collaborators.

### CORE-008 — Prefer reversible actions

Use recoverable approaches first, especially for high-risk or irreversible operations.

### CORE-009 — Validate after changes

Every meaningful change must be followed by an appropriate validation level.

### CORE-010 — Label unverified results

Clearly distinguish verified, inferred, and unverified results.

### CORE-011 — Keep documentation consistent

Documentation, configuration, and implementation must describe the same actual behavior.

### CORE-012 — Keep governance minimal

The governance project itself must not grow concepts without demonstrated value.

### CORE-013 — Continue until acceptance criteria are complete

Define clear acceptance criteria and a work list at the start. Completing one phase, changing a batch of files, or running one test is not overall completion; continue while work inside the original scope remains executable.

### CORE-014 — Execute autonomously without expanding scope

The agent may autonomously read, analyze, edit local files, and validate. Continuous execution does not authorize unrelated features, refactoring, or optimization; choose the smallest approach consistent with the existing architecture.

### CORE-015 — Analyze, fix, and revalidate failures

When a test or validation fails, do not give up, hide the error, delete a valid test, or weaken a test to obtain a green result. Analyze the cause, fix it, and rerun the applicable validation until it passes or a real blocker is confirmed.

### CORE-016 — Report evidence when blocked; never fabricate completion

Stop only after executable work is complete, required authority or external resources are unavailable, a material user decision is required, or system limits prevent continuation. Report completed work, attempts, blocker, unfinished work, and the minimum assistance needed.
