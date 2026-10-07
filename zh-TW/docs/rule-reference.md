# Rule ID 索引

Rule ID 的目的很單純：讓 Workflow、Gate、Issue 或 Review 可以引用一條穩定規則，而不依賴「第幾段」這種容易隨編輯改變的位置。

| Prefix | 文件 | 主題 |
| --- | --- | --- |
| `CORE-*` | `rules/core.md` | 核心原則 |
| `DEC-*` | `rules/decision.md` | 自主決定、詢問與授權 |
| `CONV-*` | `rules/convergence.md` | 收斂、Patch Chain、Stop-and-Reassess |
| `BOOT-*` | `rules/project-bootstrap.md` | 新專案初始化 |
| `FMT-*` | `rules/file-format.md` | 檔案格式與 Diff hygiene |
| `ENG-*` | `rules/engineering.md` | 工程、架構、依賴與資源生命週期 |
| `VAL-*` | `rules/validation.md` | 驗證層級與回報 |
| `DOC-*` | `rules/documentation.md` | 文件同步 |
| `GIT-*` | `rules/git.md` | Git 操作 |
| `REL-*` | `rules/release.md` | 發布與 Artifact |

例如 Code Review 裡寫「這個修改會觸發 `CONV-002`」就能直接表示目前開始出現補丁連鎖，而不需要把整段規則重新複製一次。

ID 一旦公開使用，最好維持語意穩定。若一條規則的意思真的完全改變，新增 ID 通常比讓舊 ID 悄悄換意思更容易追蹤。
