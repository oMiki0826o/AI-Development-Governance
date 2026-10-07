# AGENTS.md

本檔只放這個 Repository 特有、而且 Agent 每次工作都值得知道的規則。通用工作流程由 AI Development Governance 提供，不在這裡重新複製。

## Project

- Name: `<project-name>`
- Runtime / Platform: `<runtime>`
- Supported versions: `<versions>`

## Architecture Boundaries

- `<project-specific dependency direction>`
- `<module ownership rule>`
- `<public API boundary>`

## Project Layout

```text
<important project paths>
```

## Configuration and Data

- Configuration: `<path / policy>`
- Runtime data: `<path / policy>`
- Secrets: `<environment / secret store policy>`

## Validation Commands

```bash
<syntax / test / lint / build commands>
```

## Local Notes

只填真正屬於這個專案的限制。語言偏好、通用 Git、安全與驗證規則不要在這裡重抄一份。
