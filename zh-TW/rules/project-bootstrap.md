# Project Bootstrap Policy

新專案需要留下足夠的資訊讓人能理解、安裝、執行、維護與發布，但不應為了「看起來專業」預先建立沒有用途的架構。

### BOOT-001 — 最低專案內容

正式專案至少應有 README、LICENSE、`.gitignore`、依賴定義或明確的無依賴聲明、主要 Source / Project content，以及 `data/` 的基本分層。

README、LICENSE 與 `.gitignore` 的格式入口是 `templates/GithubRepoTemplate.md`。

### BOOT-002 — 依賴必須可追蹤

依技術棧使用一套正式 dependency 定義。不要同時建立多套功能重疊的 dependency system。若專案確實沒有 Runtime dependency，清楚記錄 `None` 即可，不為形式建立空 manifest。

### BOOT-003 — Runtime 與 AI 工作資料分離

`data/runtime/` 放 Database、Cache、State、PID、Log 或下載產物等執行期資料，預設不進 Git。`data/ai/` 放人類與 Agent 都可讀的專案 Context、決策、設計討論、實作計畫、交接資料與工作紀錄，不保存 Secrets。原始 AI 協作紀錄放在 `data/ai/records/`，預設由 `.gitignore` 排除；整理後且對使用者有價值的穩定結論才可寫入公開文件。

### BOOT-004 — 條件式建立目錄

`tests/`、`docs/`、`config/`、`scripts/`、`.github/`、`src/` 等只有在有實際用途時才建立。不要預先產生空的 services、repositories、managers、adapters、factories、utils 等層級。

### BOOT-005 — 初始化完成要能被使用

新專案完成前，README 與實際內容要一致、License 與 `.gitignore` 要正確、依賴能被理解、主要入口明確、Runtime data 與版本控制內容分離，且基本安裝或啟動方式已驗證或明確標示未驗證。
