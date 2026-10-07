# Git Policy

Git 指令本身能做什麼，不代表 Agent 就有權直接執行。這裡把常見操作分成讀取、受控與高風險三類。

### GIT-001 — 先查看狀態與 Diff

進行會改變 Git 狀態的工作前先確認 working tree、Branch 與相關 Diff。Commit 的基本順序是 `git status` → `git diff` → 選擇性 staging → `git diff --staged` → Pre-commit Gate → Commit。

### GIT-002 — 不盲目 staging

不要在未檢查內容時直接 `git add .`。Staged files 應對應一個合理工作單位。

### GIT-003 — Read-only 操作可自主使用

`git status`、`git diff`、`git log`、`git branch`、`git branch --show-current`、`git remote -v` 等通常可自主使用。`git fetch` 會更新 remote-tracking refs，但不直接改 working tree；仍需遵循環境權限。

### GIT-004 — 會改 Working Tree 的操作先理解影響

`git add`、`git commit`、`git switch`、`git merge`、`git pull`、`git revert` 等在執行前要理解目前 working tree 與影響範圍。有不明未提交修改時不盲目執行。

### GIT-005 — 破壞性操作需要明確授權

`git reset --hard`、`git clean -fd`、`git branch -D`、force push、history rewrite 與會丟失未提交工作的 restore 依 `DEC-004` 處理。

### GIT-006 — Commit 不為 Contribution 刻意拆碎

一個 Commit 應代表合理工作單位，訊息描述實際變更。可沿用 `feat:`、`fix:`、`refactor:`、`test:`、`docs:`、`chore:` 等專案既有慣例，避免 `update`、`final2`、`aaa` 等低資訊訊息。

### GIT-007 — Pull / Merge / Rebase 不用預設答案

`git pull` 不是「避免衝突」的萬用指令。操作前確認 Branch、Upstream 與 working tree；Merge / Rebase 依 Repository policy 決定。Conflict 不無條件選 ours 或 theirs，先理解雙方意圖。

### GIT-008 — 已公開歷史優先可追蹤回滾

已公開的歷史通常優先使用 `git revert`，而不是直接 rewrite history。若涉及資料 migration，Code rollback 與 Data rollback 分開評估。
