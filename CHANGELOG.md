# Changelog

本專案使用版本號記錄治理規範與工具的可見變更。只有會影響使用方式、規則語意或工具行為的內容才需要列入。

## 1.1.0 - 2026-10-08

### Added

- 新增 `QUICKSTART.md`。
- 為核心規則加入穩定 Rule ID。
- Gate 加入 Actor、Evidence 與 Blocking 定義。
- 新增 `scripts/validate.py` 與 GitHub Actions 驗證流程。
- 新增 `scripts/bootstrap_project.py`，提供 minimal / standard / full 三種套用模式。
- 新增 `docs/`，包含架構、使用矩陣、整合方式、實際案例與工具說明。

### Changed

- 重寫 README，使安裝、Bootstrap 與 Source ZIP 行為更清楚。
- 調整 Release Gate，只有專案實際使用 dependency manifest / lock file 時才要求驗證。
- `templates/GithubRepoTemplate.md` 改為 GitHub 文件模板入口，細節拆分到 `templates/github/`，避免單一巨型模板繼續膨脹。
- Docs 明確定位為人類閱讀文件，不具有規範權威。

## 1.0.0 - 2026-10-08

- 初版 Rule / Workflow / Gate / Template 架構。
- 建立 Decision、Convergence、Validation、Git 與 Release 等核心治理規則。
