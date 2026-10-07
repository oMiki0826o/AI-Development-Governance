# Task Lifecycle Workflow

這份流程只安排順序，不另外發明規則。

```text
Receive Task
  -> Inspect
  -> Understand
  -> Scope
  -> Risk / Decision
  -> Plan
  -> Pre-edit Gate
  -> Implement
  -> Validate
  -> Regression Review
  -> Diff Review
  -> Report
```

1. **Receive Task**：整理需求與完成條件，使用 `DEC-001`～`DEC-006` 判斷是否真的需要詢問。
2. **Inspect**：依 `CORE-001`、`CORE-002`、`ENG-001` 讀取相關架構、設定、dependency、tests 與文件。
3. **Understand**：建立目前行為與資料流模型；若是 Bug，切換到 `workflows/bugfix.md`。
4. **Scope**：依 `CORE-005` 控制修改範圍；涉及新抽象時檢查 `CONV-001` 與 `CONV-004`。
5. **Risk / Decision**：把未知事項分類為自行查證、自主決定、詢問或明確授權。
6. **Plan**：選擇符合現有架構且概念最少的方案；大任務可分成可驗證階段。
7. **Pre-edit Gate**：通過 `gates/pre-edit.md`。
8. **Implement**：依 Engineering 與 File Format Rules 修改。
9. **Validate**：依 `VAL-001`～`VAL-010` 執行與風險相符的驗證。
10. **Regression Review**：檢查受影響的舊路徑。
11. **Diff Review**：排除 Scope creep、format noise、Secrets 與意外檔案；準備 Commit 時進入 Pre-commit Gate。
12. **Report**：精確回報做了什麼、實際驗證了什麼、哪些仍未驗證，以及剩餘限制。
