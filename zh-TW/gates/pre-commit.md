# Pre-commit Gate

- **Gate ID**: `GATE-PRE-COMMIT`
- **Actor**: 準備建立 Commit 的 Agent 或開發者
- **Evidence**: `git status`、`git diff`、`git diff --staged`、實際執行的驗證命令與結果
- **Blocking**: 是。Secrets、未理解的大範圍 Diff、必要驗證失敗或 Scope 不明時不得 Commit

Commit 前確認：

- [ ] `git status` 已檢查（`GIT-001`）。
- [ ] `git diff` 已閱讀。
- [ ] Staged files 只包含本次合理工作單位（`GIT-002`）。
- [ ] `git diff --staged` 已檢查。
- [ ] 沒有 Secrets、Local DB、Log、Cache 或非預期 Artifact。
- [ ] 沒有無意義的大範圍 reformat（`FMT-008`）。
- [ ] 適用的 Syntax / Parse / Test / Lint 已實際執行，或未執行原因已記錄（`VAL-010`）。
- [ ] Regression 風險已檢查（`VAL-008`）。
- [ ] 需要同步的 Config、Example 與 Docs 已更新（`DOC-002`）。
- [ ] Commit message 能描述實際變更，且不是為刷 Contribution 刻意拆碎（`GIT-006`）。
