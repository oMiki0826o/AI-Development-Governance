# Claude Code

Claude Code 的專案入口通常是 `CLAUDE.md`。它適合放 Repository 的常用命令、重要檔案、程式風格與專案特有工作方式，概念上和這個倉庫提供的 `project-agents.md` 很接近。

如果想共用本治理倉庫，可以讓 `CLAUDE.md` 保持短小，再透過 Claude Code 支援的 `@path/to/file` 引用需要的規則。例如一般工作只引 core / decision，Release 時再讀 release workflow 與 gate，而不是把所有規範永久塞在同一份 CLAUDE.md。

對個人偏好與專案規則也建議分開。跨所有專案的個人習慣可以放在使用者層；Repository 裡只保存團隊願意一起版本控制的內容。

官方參考：

- https://docs.anthropic.com/zh-CN/docs/claude-code/memory
