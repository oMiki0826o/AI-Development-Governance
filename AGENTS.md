# AGENTS.md

本檔只說明如何維護 AI Development Governance 這個倉庫本身。平台與系統層指令仍具有更高優先級。

## Authority Model

- `rules/` 是治理規則的唯一權威來源。
- `workflows/` 只排列工作順序，不重新定義 Rule。
- `gates/` 只把既有 Rule 轉成階段性檢查，並記錄 Actor / Evidence / Blocking。
- `templates/` 只提供可重複使用的內容或入口。
- `templates/GithubRepoTemplate.md` 是 GitHub 發布文件的最高權威入口；涉及 README、LICENSE、`.gitignore`、Discord 發布文案或 Repo Description 時 MUST 先遵守本檔，再參考 `templates/github/` 的拆分模板。
- `docs/` 是給人閱讀的說明、案例與整合指南，不具有規範權威。
- `data/ai/` 只保存本倉庫的狀態、決策與工作紀錄。
- 所有 AI 與人類的專案協作紀錄、設計討論、實作計畫、交接資料與重大工作紀錄 MUST 放在 `data/ai/` 下；不得放在公開的 `docs/` 或其他產品文件目錄。
- `data/ai/records/` 預設由 `.gitignore` 排除；可公開的穩定結論必須整理後寫入適當的公開文件，不得直接公開原始協作紀錄。
- `README.md` 與 `QUICKSTART.md` 是入口文件，不是規範來源。

## Before Editing

1. 先搜尋是否已有相同或高度重疊的 Rule ID / 規則。
2. 判斷修改屬於 Rule、Workflow、Gate、Template、Tooling 或 Docs。
3. 規則語意只修改權威 Rule；其他地方只同步引用與說明。GitHub 發布文件的格式語意以 `templates/GithubRepoTemplate.md` 為準。
4. 若改動會讓 Workflow、Gate、Validator 或 Docs 過時，同一批修改中一起同步。

## Scope

- 不因單一案例加入過度專用的通用規則。
- 專案特有規則應留在該專案的 `AGENTS.md` 或專案文件。
- 新增目錄、抽象層或工具前必須有明確用途。
- 不為了看起來完整而建立空文件或空架構。
- Docs 應自然、可讀，避免寫成給模型看的命令清單或過度規範化語氣。

## Validation

修改完成後至少執行：

```bash
python3 scripts/validate.py
python3 -m py_compile scripts/*.py
```

若改動 Bootstrap，再用暫存目錄做一次 dry run 或實際建立測試。

## Change Report

完成後簡要列出修改的權威規則、受影響的 Workflow / Gate / Tooling、實際執行的驗證，以及仍存在的限制。
