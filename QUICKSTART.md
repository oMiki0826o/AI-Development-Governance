# Quick Start / 快速入門

這個專案提供可追蹤的 AI Coding Agent 工程規範，包含 Rule、Workflow、Gate、Template 與給開發者閱讀的 Docs。首次使用先從 [架構說明](zh-TW/docs/architecture.md) 閱讀。

## 安裝到自己的專案

```bash
python3 scripts/bootstrap_project.py /path/to/project --mode minimal --dry-run
python3 scripts/bootstrap_project.py /path/to/project --mode minimal
```

`minimal` 包含能直接讀取的核心 Rule 與 Workflow。需要更完整的本地規範可改用 `--mode standard` 或 `--mode full`。多語言可用 `--language bilingual`。已存在文件衝突時不會自動覆寫；確認差異後才使用 `--force`。

每個模式都會產生可用的 `AGENTS.md` 與 `.governance/manifest.json`，確保 `data/` 遵守本地忽略政策。已有工作資料不會被覆寫。更完整的說明見 [Bootstrap 指南](zh-TW/docs/tooling/bootstrap.md)。

## 驗證工具

```bash
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

Validator 只驗證可客觀判斷的結構與參照關係；不會聲稱已驗證某個程式的工程品質。

## English

Bootstrap another repository using the commands above. Add `--language en` for English or `--language bilingual` for both language editions. See the [English Bootstrap guide](en/docs/tooling/bootstrap.md) and [validation guide](en/docs/tooling/validator.md).
