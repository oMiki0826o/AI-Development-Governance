# AI Development Governance

![Version](https://img.shields.io/badge/version-1.1.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Tech](https://img.shields.io/badge/stack-Markdown%20%2B%20Python-lightgrey)

[中文](#中文) | [English](#english)

---

## 中文

### 目錄
- [關於](#關於)
- [功能](#功能)
- [安裝](#安裝)
- [使用方式](#使用方式)
- [授權](#授權)

### 關於
AI Development Governance 是一套給 AI Coding Agent 與人類協作者使用的開發治理規範。它關注的是可以觀察與驗證的工作行為，例如：如何理解任務、什麼時候應自行判斷或詢問、如何避免補丁連鎖、怎麼驗證修改，以及 Commit、Push 與 Release 前該檢查哪些內容。

這個倉庫把內容分成 Rule、Workflow、Gate、Template 與 Docs。Rule 是唯一規範來源；Workflow 只說明工作順序；Gate 負責階段性檢查；Template 提供可重複使用的輸出格式；Docs 則是給人閱讀的說明與範例，不重新定義規則。凡涉及 GitHub 發布文件，優先遵守 [`GithubRepoTemplate.md`](./zh-TW/templates/GithubRepoTemplate.md)，其他 GitHub 子模板只能補充它。

所有 AI 協作文件、工作計畫、交接資料與本地執行資料都放在 `data/`，而且 `data/` 必須整體被 `.gitignore` 忽略，不會發布到 GitHub。

### 功能
- 提供任務理解、決策權限、工程修改、驗證、Git 與 Release 的核心規則。
- 提供 Stop-and-Reassess、Patch Chain 與 Complexity Budget，避免問題越修越複雜。
- 使用 Rule ID 讓 Workflow、Gate 與文件可以穩定引用同一條規則。
- 提供 Pre-edit、Pre-commit、Pre-push 與 Pre-release Gate，並定義檢查者與應保留的證據。
- 提供 `scripts/validate.py` 檢查倉庫完整性，以及 `scripts/bootstrap_project.py` 將治理入口套用到其他專案。
- 提供 Codex、Claude Code、GitHub Copilot 與 Cursor 的整合說明與完整工作範例。

### 安裝
若從 Git 使用：

```bash
git clone https://github.com/<owner>/AI-Development-Governance.git
cd AI-Development-Governance
python3 scripts/validate.py
```

若使用 Release ZIP，解壓後直接執行 Validator 即可。ZIP 是 source package，刻意不包含 `.git/`；需要獨立 Git repository 時再執行 `git init` 或從 GitHub Clone。

### 使用方式
第一次使用建議先閱讀 [QUICKSTART.md](./QUICKSTART.md)。本倉庫提供 [繁體中文規範](./zh-TW/) 與 [English specification](./en/)。一般任務不需要把整個倉庫塞進 Agent Context；中文使用矩陣見 [zh-TW/docs/usage-matrix.md](./zh-TW/docs/usage-matrix.md)，英文使用矩陣見 [en/docs/usage-matrix.md](./en/docs/usage-matrix.md)。

快速套用到另一個專案：

```bash
python3 scripts/bootstrap_project.py /path/to/project
```

預設只建立專案級 `AGENTS.md` 與 `data/ai/`。若希望把治理規則一起 vendoring 到專案，可使用 `--mode standard` 或 `--mode full`；詳細說明見 [中文 Bootstrap 工具說明](./zh-TW/docs/tooling/bootstrap.md) 或 [English bootstrap guide](./en/docs/tooling/bootstrap.md)。

### 授權
本專案採用 MIT License 授權，詳見 [LICENSE](./LICENSE)。

---

## English

### Table of Contents
- [About](#about)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

### About
AI Development Governance is a development workflow specification for AI coding agents and human collaborators. It focuses on observable, verifiable engineering behavior: understanding a task, deciding when to act or ask, avoiding patch chains, validating changes, and checking work before commit, push, and release.

The repository separates Rules, Workflows, Gates, Templates, and Docs. Rules are authoritative; workflows sequence those rules; gates define readiness checks; templates provide reusable output structures; and docs explain how the pieces are used without redefining policy. For GitHub publication files, [`GithubRepoTemplate.md`](./en/templates/GithubRepoTemplate.md) has the highest template authority.

All AI collaboration documents, work plans, handoff material, and local runtime data belong under `data/`. The entire `data/` directory MUST be ignored by `.gitignore` and is not published to GitHub.

### Features
- Core policies for task scope, decision authority, engineering, validation, Git, and releases.
- Stop-and-Reassess, Patch Chain, and Complexity Budget guidance to keep fixes from accumulating unnecessary layers.
- Stable Rule IDs for cross-references from workflows and gates.
- Pre-edit, pre-commit, pre-push, and pre-release gates with actors and evidence expectations.
- A repository validator and a project bootstrap tool written with the Python standard library.
- Integration notes for Codex, Claude Code, GitHub Copilot, and Cursor, plus end-to-end examples.

### Installation
Clone the repository and run the validator:

```bash
git clone https://github.com/<owner>/AI-Development-Governance.git
cd AI-Development-Governance
python3 scripts/validate.py
```

Release ZIPs are source packages and intentionally do not contain `.git/`. Initialize a repository separately if needed.

### Usage
Start with [QUICKSTART.md](./QUICKSTART.md). Choose the [English specification](./en/) or [Traditional Chinese specification](./zh-TW/). Agents do not need the whole repository in context for every task; use the [English usage matrix](./en/docs/usage-matrix.md) or [Chinese usage matrix](./zh-TW/docs/usage-matrix.md) to load only what is relevant.

Bootstrap another project with:

```bash
python3 scripts/bootstrap_project.py /path/to/project
```

### License
This project is licensed under the MIT License, see [LICENSE](./LICENSE).
