# Bootstrap Project

`scripts/bootstrap_project.py` 用來把這套治理方式套進另一個 Repository，不需要手動複製一堆檔案。

最常用的是預設模式：

```bash
python3 scripts/bootstrap_project.py /path/to/project
```

它會加入一份專案級 `AGENTS.md`、`data/ai/project-memory.md` 與 records 目錄。原本已存在的檔案不會被覆蓋。

## 三種模式

### minimal

只加入專案入口與 AI 工作資料。適合治理倉庫在別處可讀，或只想先整理 Repository 規則的專案。

### standard

除了 minimal 內容，也把最常用的 Rules、Task / Bugfix Workflow 與日常 Gate 複製到 `.governance/`。適合希望規範跟著 Repository 一起版本控制，但不需要 Release 全套文件的情況。

### full

把 Rules、Workflows、Gates 與 GitHub Template 全部 vendoring 到 `.governance/`。適合需要離線、自包含或正式團隊共用的 Repository。

```bash
python3 scripts/bootstrap_project.py /path/to/project --mode full
```

Vendored 規則是某一版的 snapshot。之後若 Governance 上游更新，不應悄悄覆蓋專案內已修改的版本；先 Review diff，再決定是否更新。

## 覆蓋既有檔案

預設遇到衝突會停止並列出檔案。只有確定要覆蓋時才使用：

```bash
python3 scripts/bootstrap_project.py /path/to/project --force
```

這個選項不應拿來當一般更新機制。
