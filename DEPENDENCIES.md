# Dependencies

這個倉庫的治理內容本身是 Markdown，不需要安裝任何第三方 Runtime dependency。

## 文件使用

- Runtime dependency: None.

## Repository tooling

`scripts/validate.py` 與 `scripts/bootstrap_project.py` 使用 Python 標準函式庫，建議 Python 3.11 或更新版本。

不需要 `pip install` 額外套件。

GitHub Actions 只負責執行上述腳本與 Python compile check。
