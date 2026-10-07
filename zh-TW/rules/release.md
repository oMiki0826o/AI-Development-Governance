# Release Policy

### REL-001 — Release 有自己的完成條件

程式修改完成不代表可以發布。Release 前要確認 Version、適用測試、Regression、文件、設定範例、Repository cleanliness、Secrets、Git 狀態與 Breaking change / migration 記錄。

### REL-002 — Version 只有一個 Source of Truth

版本號應有清楚的權威來源。若專案採 Semantic Versioning 或其他既有政策，沿用該政策；不為了發布外觀任意升版。

### REL-003 — Dependency 檢查只在適用時要求

如果專案有 dependency manifest、lock file 或 build metadata，發布前檢查它們與實際依賴一致。確實沒有 Runtime dependency 的文件型專案，不為了 Gate 形式建立空 manifest。

### REL-004 — Artifact 建立後重新驗證

ZIP、JAR、Wheel、Binary 或其他 Artifact 產生後要驗證 Artifact 本身：能開啟或解壓、必要檔案存在、沒有 Secrets / Local DB / Log / Cache / Virtual Environment 等不應發布內容，Version 與 metadata 一致。Source tree 通過測試不代表 Artifact 一定正確。

### REL-005 — 可行時做乾淨環境驗證

重要 Release 若合理可行，從乾淨目錄或環境做最小安裝 / 啟動驗證，避免依賴開發機上未宣告的 package、local file 或 environment state。

### REL-006 — Release Notes 只描述實際內容

不要把未完成、未合併或未驗證內容寫成已發布功能。重大 Release 應清楚指出 New / Changed / Fixed、Breaking changes、Migration、Known limitations 與 Compatibility。

### REL-007 — Tag / Publish 遵循授權邊界

建立 Tag、GitHub Release 或其他外部發布前通過 Pre-release Gate；外部動作與不可逆操作依 `rules/decision.md` 的授權層級執行。
