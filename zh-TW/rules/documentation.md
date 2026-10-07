# Documentation Policy

### DOC-001 — 文件反映實際狀態

文件、設定與程式行為衝突時，先確認實際狀態，再修正過時文件。README、LICENSE、`.gitignore` 與發布文案的格式入口是 `templates/GithubRepoTemplate.md`。

### DOC-002 — 變更契約時同步文件

Public API、Config、CLI、Dependency / Installation、Features、Compatibility 或 Breaking change 有變化時，同步相關 Usage、Example、Migration 或 Release notes。

### DOC-003 — 不描述不存在的內容

不得加入尚未實作的功能、不存在的 Command / Config、未驗證的平台支援、虛假的 Badge、Release、Screenshot 或 Benchmark。規劃內容要清楚標示為規劃。

### DOC-004 — README 保持入口角色

README 負責讓人理解專案與開始使用；Architecture、Configuration、API 或 Deployment 明顯超出 README 合理範圍時，再建立 `docs/`。不要為同一內容建立多份近似文件。
