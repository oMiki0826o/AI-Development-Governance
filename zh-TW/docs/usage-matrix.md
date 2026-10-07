# 什麼情況要讀哪些文件

不建議每次任務都把整個倉庫餵給 Agent。大多數工作只需要核心規則，再加上當下情境真正相關的幾份文件。

| 情境 | 建議先讀 | 需要時再讀 |
| --- | --- | --- |
| 一般程式修改 | `rules/core.md`, `rules/decision.md`, `workflows/task-lifecycle.md` | `rules/engineering.md`, `rules/file-format.md` |
| Bug 修復 | `workflows/bugfix.md`, `rules/validation.md` | `rules/convergence.md` |
| 大型重構 | `rules/engineering.md`, `rules/convergence.md` | `rules/decision.md`, `rules/validation.md` |
| 建立新專案 | `rules/project-bootstrap.md` | `templates/GithubRepoTemplate.md` |
| 編寫 README / LICENSE | `templates/GithubRepoTemplate.md` | `rules/documentation.md` |
| 準備 Commit | `rules/git.md`, `gates/pre-commit.md` | `rules/validation.md` |
| 準備 Push | `rules/git.md`, `gates/pre-push.md` | Repository 自己的 Git policy |
| 準備 Release | `workflows/release.md`, `rules/release.md`, `gates/pre-release.md` | `templates/GithubRepoTemplate.md` |

如果專案已經有自己的 `AGENTS.md`、`CONTRIBUTING.md` 或架構文件，也要一起看。通用治理規範的目的不是蓋掉專案慣例，而是補足跨專案都容易出問題的工作流程。

## 常駐內容應該多短

對支援 Repository instruction 的 Agent，常駐檔案最好只放每次工作都真的有用的內容：專案入口、架構邊界、常用驗證指令、不能碰的資料、以及幾條高價值工作規則。

完整 Validation、Release 或 Git 細節可以按任務讀取。這樣比把數十頁規範永遠放在 Context 裡更容易維護，也比較不會讓重要規則被大量低價值文字淹沒。
