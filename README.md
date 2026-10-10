# AI Development Governance

![Version](https://img.shields.io/badge/version-1.2.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Tech](https://img.shields.io/badge/stack-Markdown%20%2B%20Python-lightgrey)

[中文](#中文) | [English](#english)

## 中文

### 關於

這是一套供 AI Coding Agent 與開發者共同使用的工程治理規範。它規範任務理解、決策授權、收斂修改、驗證證據與正式發布，目標是在減少重複指令的同時保留可審查的結果。

Rule 為權威來源，Workflow 安排順序，Gate 提供檢查點，Template 提供可重用格式，Docs 則用一般工程文件的方式解釋用途。

### 功能

- 穩定的雙語 Rule ID，以及可驗證的 Gate 與引用關係。
- `bootstrap_project.py` 支援 `minimal` / `standard` / `full` 以及 `zh-TW` / `en` / `bilingual`。
- 完整的本地工作資料隔離：`data/` 一律忽略，且不會在更新時覆寫既有工作紀錄。
- 使用 SHA-256 的安裝資訊清單，方便辨識來源版本及檔案。
- `validate.py` 檢查文本、內部 Markdown 連結與錨點、規則識別碼、雙語結構及發行版本。
- 內建測試與 GitHub Actions，包含實際初始化測試。

### 安裝

```bash
unzip AI-Development-Governance-v1.2.0-optimized.zip
cd AI-Development-Governance-v1.2.0
python3 scripts/validate.py
```

這是以公開倉庫內容為基礎，經審核後整合的修正版原始碼。不需要安裝第三方 Python 套件；直接執行 Validator 與測試即可。

### 使用方式

```bash
python3 scripts/bootstrap_project.py /path/to/project --mode standard --language zh-TW --dry-run
python3 scripts/bootstrap_project.py /path/to/project --mode standard --language zh-TW
python3 -m unittest discover -s tests -v
```

詳細修正記錄請參閱 [交付說明](REVIEW_NOTES.md)。如需更新已存在的文件，必須先審核差異，再使用 `--force`；本地工作記錄永遠不會被安裝程序覆寫。閱讀 [快速入門](QUICKSTART.md)、[架構說明](zh-TW/docs/architecture.md) 或 [驗證器說明](zh-TW/docs/tooling/validator.md) 了解更多。

### 授權

採用 MIT License，詳見 [LICENSE](LICENSE)。

## English

### About

AI Development Governance offers practical policies for AI coding agents and human developers, covering task scope, engineering decisions, convergence, validation evidence and releases. Rules are authoritative, workflows establish task order, gates define review checkpoints, templates provide reusable forms and docs explain the design.

### Features

- Stable bilingual Rule IDs, gate metadata and reference checks.
- Three bootstrap modes and Traditional Chinese, English or bilingual installation.
- Safe local `data/` policy with preservation of existing work records.
- SHA-256 installation manifest and clear vendor paths.
- Repository validation and executable integration tests in CI.

### Installation

```bash
unzip AI-Development-Governance-v1.2.0-optimized.zip
cd AI-Development-Governance-v1.2.0
python3 scripts/validate.py
```

This is a reviewed and merged repaired source distribution based on the public repository. It requires no third-party Python dependencies; run the validator and test suite before use.

### Usage

```bash
python3 scripts/bootstrap_project.py /path/to/project --mode full --language en --dry-run
python3 scripts/bootstrap_project.py /path/to/project --mode full --language en
python3 -m unittest discover -s tests -v
```

See [delivery and validation notes](REVIEW_NOTES.md), the [quick start](QUICKSTART.md), [architecture](en/docs/architecture.md) and [Bootstrap guide](en/docs/tooling/bootstrap.md). Review local modifications before `--force`; existing `data/ai/` work is always preserved.

### License

Licensed under [MIT](LICENSE).
