# v1.2.0 重建修正版交付說明

本交付物以 `oMiki0826o/AI-Development-Governance` 公開倉庫截至 `9774439d886de86ea9fc2d534f98dbfc3c247643` 的已檢查內容為基礎。由於執行環境未能直接 Clone GitHub 原始碼，這份產物是依已讀取的倉庫結構、程式碼與規範重新整理後，經審核合併的**可執行完整專案**，不是原始倉庫的逐位元組 Patch。部分說明文件已濃縮及改寫；後續應以 Validator、測試與自身規範持續檢查。

## 修正與增強

- 修正 standard 模式多出一層 `.governance`、full 模式產生重複樹狀結構的問題。
- minimal / standard / full 在 zh-TW、en 與 bilingual 組合下都生成有效的 Agent 入口與 Rule 路徑。
- Bootstrap 維護 `.gitignore` 的 `data/` 規範，保留既有內容並拒絕明顯的取消忽略例外。
- 預設在既有檔案衝突時拒絕操作；`--force` 仍保留所有既有 `data/ai/` 工作紀錄。
- Bootstrap 增加路徑與 Symbolic Link 安全檢查、預先檢查目的地、寫入失敗回復及不會修改檔案的 `--dry-run`。
- 產生 `.governance/manifest.json`，記錄版本、模式、語言與管理檔案 SHA-256。
- Validator 缺檔與無效 UTF-8 時會回報錯誤，不會因讀取遺失的 VERSION / README 中途崩潰。
- 補上 Markdown 內部連結、圖片連結、章節錨點、Reference-style Link、Rule ID 引用、Gate metadata 與完整 SemVer 檢查。
- 解決 `data/` 是否整體忽略的文件衝突，繁體中文與英文皆採一致的 Rule ID 與資料隔離模式。
- 發布模板依工作用途拆分，保留雙語 README、Discord 一般工具與 Minecraft 機器、授權及忽略規則的撰寫範例。
- CI 設定包含 Python 3.11 與 3.13，並實際執行標準函式庫單元與整合測試。

## 已執行驗證

在本地 Python 3.13.5 環境執行：

```bash
python3 scripts/validate.py
python3 -m py_compile scripts/*.py
python3 -m unittest discover -s tests -v
```

結果：Validator 通過，編譯通過，**39 個測試通過**。測試涵蓋 3 種 Bootstrap 模式 × 3 種語言選擇、實際檔案輸出、覆寫與衝突、工作資料保留、路徑安全、回復機制，以及 Validator 正反案例。

CI 的 Python 3.11 / 3.13 Matrix 是設定檔，本次並未在 GitHub Actions 上執行修正版；不能把 CI 設定視為已在線上通過。

## 已知限制

- GitHub Markdown 的特殊擴充語法可能仍須人為檢查；Validator 的 Anchor/Reference Parser 是輕量工具，不是完整 Markdown Renderer。
- 英文與繁體中文是條款識別碼與主要行為對齊，未進行人工法律性質的逐字等價審查。
- 本版尚無上游規則三向合併器。`--force` 可能覆寫 AGENTS 與 `.governance/` 已編輯的檔案，使用前務必審查差異；不會覆寫 `data/ai/`。
- Linux/macOS 的一般 Python 檔案操作已測試；跨平台檔案權限與 Windows Symbolic Link 行為未進行實機測試。
- 本版已整合至本地 `main`；遠端同步狀態以 GitHub 與最後一次 Push 結果為準。
