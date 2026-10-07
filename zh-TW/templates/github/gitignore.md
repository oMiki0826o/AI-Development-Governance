# .gitignore Template Policy

`.gitignore` 應依實際技術棧組合，不整包複製所有語言模板。

通常會考慮：

- OS / Editor：`.DS_Store`、IDE metadata、swap files。
- Secrets / local environment：`.env`、本機 credentials。
- Runtime：Database、Log、Cache、PID、下載產物。
- Language / framework：`__pycache__/`、`node_modules/`、Gradle build output 等實際會出現的內容。
- Release / Build artifact：是否忽略依專案發布方式決定。

`data/` 不應整個忽略。如果 `data/ai/` 是版本控制的專案記憶，而 `data/runtime/` 是執行資料，應只忽略 Runtime 區域。
