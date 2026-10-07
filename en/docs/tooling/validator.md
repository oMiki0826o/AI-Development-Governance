# Validator

Run the repository validator from the project root:

```bash
python3 scripts/validate.py
```

It checks objective invariants: required files, UTF-8 and LF formatting, final newlines, relative Markdown links, matching Rule and Gate IDs, version consistency, and Gate metadata. It does not judge policy quality or replace tests, review, or real-environment verification.
