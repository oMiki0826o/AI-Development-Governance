# Cursor

Cursor 支援 `.cursor/rules` 的 Project Rules，也支援較簡單的 `AGENTS.md`。如果專案只需要一份 Repository 級入口，先從 AGENTS 開始通常就夠；真的需要依檔案類型或目錄套用不同規則時，再拆成 `.cursor/rules/*.mdc`。

本治理倉庫不建議為了「支援 Cursor」就把每份 Rule 各複製成一個 `.mdc`。比較好的方式是讓 Cursor 的規則檔說明何時應讀 `rules/validation.md`、`rules/git.md` 等原始文件，保持單一權威來源。

如果使用 bootstrap 的 `standard` 或 `full` 模式，vendored 規範會放在 `.governance/`，Cursor Rule 可以直接指向那裡。

官方參考：

- https://cursor.com/docs/rules
