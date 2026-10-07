# GitHub Copilot

GitHub Copilot 可以使用 Repository-wide instructions，常見位置是 `.github/copilot-instructions.md`。需要更細的範圍時，也能用 `.github/instructions/**/*.instructions.md` 做 path-specific instructions。部分 Copilot Agent / Code Review 工作流也支援 `AGENTS.md`。

對這套 Governance 來說，建議把 `.github/copilot-instructions.md` 當成輕量入口，只放 Repository 特有資訊與「什麼情況去讀哪份治理文件」。如果每一條通用 Rule 都再複製一份進去，之後很快就會產生兩個 Source of Truth。

Path-specific instructions 比較適合真的有不同技術區域的 monorepo，例如 frontend 與 backend 的工具、測試方式差很多；小型專案通常不需要一開始就拆很多份。

官方參考：

- https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions
- https://docs.github.com/en/copilot/reference/custom-instructions-support
