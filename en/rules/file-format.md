# File Format Policy

### FMT-001 — Default text format

Unless the project specifies otherwise, use UTF-8, LF line endings, one final newline, and no meaningless trailing whitespace.

### FMT-002 — Project formatters take priority

Follow project formatter or linter settings, then `.editorconfig` / `.gitattributes`, then existing project style, then governance defaults.

### FMT-003 — Keep naming and indentation consistent

Follow the established naming and indentation style of the project.

### FMT-004 — Parse structured files after changes

Validate JSON, YAML, TOML, and other structured files with their appropriate parser.

### FMT-005 — Keep Markdown readable

Preserve headings, links, lists, code fences, and document structure.

### FMT-006 — Separate secrets and examples

Never commit secrets; use safe example configuration instead.

### FMT-007 — Separate source, runtime, generated, and artifacts

Do not mix generated or runtime output with maintained source files.

### FMT-008 — Avoid formatting noise

Do not reformat unrelated files or large sections during a focused change.

### FMT-009 — Do not migrate formats by preference

Format migrations require a concrete engineering reason and appropriate decision authority.
