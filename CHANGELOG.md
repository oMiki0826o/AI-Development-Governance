# Changelog

## 1.2.0 - 2026-10-11

### Fixed

- Corrected Bootstrap mapping across minimal, standard and full modes.
- Ensured the local `data/` ignore policy is applied without overwriting existing project rules or work records.
- Prevented installation through symlink paths and added rollback for failed installation steps.
- Replaced placeholder-only agent entry files with usable references to vendored governance policies.
- Made Validator report missing and malformed files without uncaught exceptions.

### Improved

- Added manifest checksums, Markdown link and heading-anchor validation, Rule ID references and Gate metadata checks.
- Standardized the bilingual policy identifiers and local-data model.
- Added real Bootstrap integration tests and CI matrix checks across supported modes and languages.
- Reorganized publishing templates to remove conflicting or duplicated normative policy.

### Notes

- This is a reconstructed and repaired distribution based on the reviewed public repository; wording in some explanatory documents has been consolidated.
- Automated validation checks objective invariants, not the semantic quality of engineering decisions.

## 1.1.0 - 2026-10-08

- Rule ID, Gate metadata, quick start, Validator and Bootstrap introduced.

## 1.0.0 - 2026-10-08

- Original governance policy and template hierarchy.
