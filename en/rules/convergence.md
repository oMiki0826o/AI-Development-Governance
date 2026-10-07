# Convergence and Failure Loop Policy

### CONV-001 — New abstractions must reduce complexity

An abstraction needs a stable responsibility and must reduce duplication, coupling, or unclear boundaries.

### CONV-002 — Detect patch chains

When Patch A requires B and B requires C or more workarounds, reassess A instead of treating patch count as progress.

### CONV-003 — Stop and reassess failure loops

When substantially different fixes reproduce the same failure, stop editing and rebuild the evidence and root-cause model.

### CONV-004 — Use a complexity budget

After a large change, review new concepts, overlap, removable workarounds, and maintenance cost.
