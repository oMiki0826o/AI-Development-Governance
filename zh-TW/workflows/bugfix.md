# Bugfix Workflow

```text
Reproduce / Observe
  -> Collect Evidence
  -> Trace
  -> Root Cause Hypothesis
  -> Verify Hypothesis
  -> Fix
  -> Validate
  -> Regression
  -> Close or Reassess
```

- **Reproduce / Observe**：先確認錯誤實際表現；無法重現時保存完整 Log、Stack trace、input 與環境資訊，遵循 `CORE-002`、`CORE-003`。
- **Collect Evidence**：取得直接相關的 Error、Runtime state、Config、Version 與近期 Diff。
- **Trace**：建立 Call Chain、Data Flow 或 Resource Lifecycle，找錯誤第一次偏離預期的位置。
- **Root Cause Hypothesis**：提出可被證偽的原因假設，先設計最小驗證方式。
- **Verify Hypothesis**：證據不支持時回到 Trace，不用 workaround 維持原方案。
- **Fix**：依 `CORE-004`、`ENG-002` 採用最小合理修正。
- **Validate / Regression**：依 Validation Rules 執行實際測試。
- **Close or Reassess**：若符合 `CONV-002` 或 `CONV-003`，停止補丁連鎖並重新分析。
