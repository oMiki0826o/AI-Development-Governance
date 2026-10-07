# Pre-release Gate

- **Gate ID**: `GATE-PRE-RELEASE`
- **Actor**: Release owner；可由 Agent 執行檢查，但外部發布仍受授權政策限制
- **Evidence**: Release scope、Version、驗證結果、Git 狀態、Release notes、Artifact 檢查結果；適用時包含 dependency metadata
- **Blocking**: 是。Artifact 尚未驗證、Secrets、Version 漂移、必要測試失敗或發布授權不足時不得 Release

正式發布前確認：

- [ ] Release scope 與 Version 已確定（`REL-001`, `REL-002`）。
- [ ] Version 在所有必要位置一致。
- [ ] 適用測試已執行，結果已記錄。
- [ ] Regression 狀態已確認。
- [ ] README / Docs / Config example 與實作一致。
- [ ] 若專案使用 dependency manifest / lock file，它們與實際依賴一致（`REL-003`）。
- [ ] Repository 無 Secrets、Runtime data、Debug dump 或不必要 Cache。
- [ ] Git Branch、Commit 與 working tree 狀態明確。
- [ ] Breaking changes 與 Migration 已記錄。
- [ ] Release notes 只描述實際包含內容（`REL-006`）。
- [ ] Artifact 已建立並重新開啟或解壓驗證（`REL-004`）。
- [ ] Artifact 不含禁止檔案且必要檔案完整。
- [ ] 合理可行時已做乾淨環境最小驗證（`REL-005`）。
- [ ] 未驗證的平台或外部服務已明確標示（`CORE-010`）。
- [ ] Tag / Publish 已取得適用授權（`REL-007`）。
