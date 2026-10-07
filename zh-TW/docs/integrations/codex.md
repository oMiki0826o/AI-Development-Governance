# Codex

Codex 會讀取 `AGENTS.md`，而且可以依目錄層級套用更靠近工作目錄的指令。實際使用時，最簡單的做法是在 Repository 根目錄保留一份短的 `AGENTS.md`，只寫這個專案真正特有的資訊，例如架構邊界、常用測試命令與資料位置。

不要把整套治理規範直接複製進 `AGENTS.md`。如果規範已 vendoring 到 `.governance/`，可以在專案 AGENTS 裡告訴 Codex：一般工作先讀 core / decision / task lifecycle，遇到 Bug、Git 或 Release 再讀相應文件。

Codex 對大型任務也適合使用獨立計畫文件，而不是不斷把臨時規劃塞回 AGENTS。這和本倉庫把「長期規則」與「單次工作紀錄」分開的想法是一致的。

官方參考：

- https://developers.openai.com/cookbook/examples/gpt-5/codex_prompting_guide
- https://developers.openai.com/cookbook/articles/codex_exec_plans
