# Validator

`scripts/validate.py` 是這個倉庫的基本自我檢查工具。它只處理能客觀判定的問題，不嘗試取代 Code Review。

執行方式：

```bash
python3 scripts/validate.py
```

目前會檢查：

- 必要檔案與目錄是否存在。
- 文字檔能否以 UTF-8 讀取。
- 是否混入 CRLF / CR。
- 是否有檔尾換行。
- Markdown 相對連結指向的檔案是否存在。
- Rule ID 是否重複，以及每份 Rule 是否至少有一個 ID。
- Gate 是否包含 Gate ID、Actor、Evidence 與 Blocking。
- `VERSION` 是否符合基本 SemVer，README Version badge 與 Changelog 最新版本是否一致。
- README 的 License badge 是否和目前 MIT License 一致。

成功時 Exit Code 為 0；任何檢查失敗時會列出問題並回傳非 0，方便 GitHub Actions 直接阻擋錯誤變更。

它刻意不檢查「Rule 是否夠好」、「架構是不是最佳解」這類需要工程判斷的問題。把這些也硬塞進腳本，反而會讓 Validator 變得難以信任。
