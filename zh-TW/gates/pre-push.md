# Pre-push Gate

- **Gate ID**: `GATE-PRE-PUSH`
- **Actor**: 準備把 Commit 傳到遠端的 Agent 或開發者
- **Evidence**: 目前 Branch、Remote / Upstream、待 Push Commit、Working tree 狀態與適用驗證結果
- **Blocking**: 是。Remote / Branch 不明、含敏感資料或涉及未授權 history rewrite 時不得 Push

Push 前確認：

- [ ] 目前 Branch 正確。
- [ ] Remote 與 Upstream 正確。
- [ ] 預計 Push 的 Commit 已檢查。
- [ ] Working tree 狀態已確認。
- [ ] Pre-commit 要求仍成立。
- [ ] 沒有 Secrets 或不應公開的資料。
- [ ] 已知 CI / Build requirements 沒有被忽略。
- [ ] Push 不會意外包含其他人的未完成工作（`CORE-007`）。
- [ ] Force push / history rewrite 若存在，已取得 `DEC-004` 明確授權（`GIT-005`）。
