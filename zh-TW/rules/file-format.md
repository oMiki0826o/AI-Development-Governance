# File Format Policy

### FMT-001 — 文字檔預設格式

除非專案已有明確設定，新建或修改的純文字檔預設使用 UTF-8、LF (`\n`)、單一檔尾換行，並移除無意義 trailing whitespace。不要任意加入 BOM。Binary、Database、Archive、Image、JAR 等不套用文字編碼檢查。

### FMT-002 — 專案 formatter 優先

格式權威順序為：Project formatter / linter configuration、`.editorconfig` / `.gitattributes`、既有專案風格，最後才是通用預設。通用規範不能破壞 Repository 已有格式契約。

### FMT-003 — 命名與縮排保持一致

遵循語言、Framework 與同一區域既有風格。沒有其他規則時，Python / Java 使用 4 spaces，JSON / YAML / JavaScript / TypeScript / HTML / CSS 使用 2 spaces；不無意義混用 Tab 與 Space。

### FMT-004 — Structured file 修改後要 Parse

JSON 不使用 Comment 或 trailing comma；YAML 不使用 Tab；TOML 保持合理 section；這些格式修改後應使用相應 Parser 或工具驗證。

### FMT-005 — Markdown 保持結構可讀

標題層級要合理，Code block 標示語言或內容類型，內部相對連結應能解析。README 的出版格式遵循 `templates/GithubRepoTemplate.md`。

### FMT-006 — Secrets 與 Example 分離

`.env` 與含秘密的實際設定不得提交。可提供 `.env.example` 或其他 example config，但內容不能含真實 Secrets，且結構要與目前 Schema 同步。

### FMT-007 — 區分 Source、Runtime、Generated 與 Artifact

先判斷檔案角色再決定是否版本控制。Runtime data 預設不進 Git；能穩定重建的 generated output 通常不提交，除非部署方式或專案契約要求；Binary / Archive 是否提交依專案性質判斷，不一律禁止。

### FMT-008 — 避免 Formatting Noise

局部修改不應無意義重排整個大型檔案。除非任務本身是格式整理，格式變動限制在必要區域，讓真正的邏輯修改仍然容易 Review。

### FMT-009 — 不自行做格式 Migration

不得單純因偏好把 JSON 改 YAML、`requirements.txt` 改 `pyproject.toml` 或進行其他格式 migration。這類變更需要明確工程理由，並依 `rules/decision.md` 判斷是否要詢問。
