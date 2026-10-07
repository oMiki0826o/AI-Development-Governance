# Bootstrap Tool

Use the bootstrap tool to add a governance entry point to another project without copying the entire repository into one prompt.

```bash
python3 scripts/bootstrap_project.py /path/to/project --language en
```

Supported modes are `minimal`, `standard`, and `full`. Existing files are not overwritten unless `--force` is explicitly provided. Use `--language bilingual` to install both language entry points.
