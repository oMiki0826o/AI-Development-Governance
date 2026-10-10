# Quick Start

這份文件用最短路徑說明怎麼開始使用 AI Development Governance。完整設計理由依語言放在 `zh-TW/docs/` 與 `en/docs/`，真正具有約束力的內容則在對應語言的 `rules/` 與 `gates/`。

## 先理解五個目錄

- `zh-TW/`：繁體中文規範、流程、Gate、Template 與 Docs。
- `en/`：English rules, workflows, gates, templates, and docs。
- `scripts/`：共用的 Validator 與 Bootstrap 工具。
- `data/`：本地 AI 協作與執行資料，整體不進 Git。

如果只記得一件事：**不要把同一條規則複製到多個地方。** 規則只改 `rules/` 的權威來源，其他文件引用它。

另一個重要原則是：先列出 Acceptance Criteria，再持續完成原始 Scope 內仍可執行的工作。測試失敗時要分析、修復、重新驗證；只有遇到真實阻塞時才中斷並回報證據。

## 一般任務怎麼用

大多數程式修改只需要這幾份：

1. `zh-TW/rules/core.md` 或 `en/rules/core.md`
2. `zh-TW/rules/decision.md` 或 `en/rules/decision.md`
3. 對應語言的 `workflows/task-lifecycle.md`
4. 與任務直接相關的語言規則，例如 `rules/engineering.md` 或 `rules/validation.md`

Bug 修復再加 `workflows/bugfix.md` 與 `rules/convergence.md`。準備 Commit 或 Release 時，再讀對應的 Git / Release Rule 與 Gate。

更完整的對照表在 `zh-TW/docs/usage-matrix.md` 或 `en/docs/usage-matrix.md`。

## 套用到自己的專案

最簡單的方式：

```bash
python3 scripts/bootstrap_project.py /path/to/project
```

這會建立：

```text
AGENTS.md
data/
└── ai/
    ├── project-memory.md
    └── records/
```

工具不會覆蓋已存在的檔案，除非明確使用 `--force`。一般情況下先用預設的 `minimal` 模式就夠了。

如果希望專案在離線或沒有外部治理倉庫時仍能讀到完整規則，可以選擇：

```bash
python3 scripts/bootstrap_project.py /path/to/project --mode standard
```

或：

```bash
python3 scripts/bootstrap_project.py /path/to/project --mode full
```

## 一次完整任務大概長什麼樣子

假設要修一個設定載入 Bug：

1. 先看 `git status`，確認不會蓋掉別人的工作。
2. 讀設定入口、相關 caller、schema 與測試。
3. 重現錯誤，確認真正失敗位置。
4. 如果資訊可從 repo 查到就自己查；只有會改變契約的未知事項才詢問。
5. 通過 Pre-edit Gate 後修改。
6. 執行最小相關測試，再做必要的 regression 檢查。
7. 看最終 diff，確認沒有順便重排整個檔案或增加無關抽象。
8. 要 Commit 時再通過 Pre-commit Gate。
9. 最後回報「實際做了什麼、真的跑過哪些驗證、哪些還沒驗證」。

完整範例見 `zh-TW/docs/examples/` 或 `en/docs/examples/`。

## 驗證這個治理倉庫

```bash
python3 scripts/validate.py
```

Validator 目前只檢查客觀、可自動化的項目，例如 UTF-8 / LF、內部 Markdown 連結、Rule ID 重複、版本一致性、必要檔案與 Gate metadata。它不會假裝能自動判斷「這條工程規則是不是好規則」。

## 常見用錯方式

- 把整個倉庫內容貼成一個超長 System Prompt。
- 在 Workflow 裡重新寫一遍 Rule，導致之後兩份內容不一致。
- 看到一點模糊就停止工作並追問，其實資料可以從 repo 找到。
- 修 Bug 失敗後一直加 fallback，而沒有重新驗證 root cause。
- 只跑 Syntax Check 就寫成「功能測試通過」。
- 為了讓專案看起來完整，預先建立一堆沒有用途的 manager、adapter、docs 或 scripts。
