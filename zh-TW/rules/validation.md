# Validation Policy

驗證結果必須和實際執行的檢查層級一致。這份規則的重點不是「多跑幾個命令」，而是不要把低層檢查描述成完整功能驗證。

### VAL-001 — Level 0: Inspection

只閱讀程式碼、Diff、設定與文件。可以提出分析，但不能宣稱程式已通過執行驗證。

### VAL-002 — Level 1: Syntax / Parse / Compile

確認語法、Structured file Parser 或 Compiler 接受內容。只能證明相應階段通過。

### VAL-003 — Level 2: Static Analysis

Lint、Type Check、Import analysis 等。工具未實際執行時不得聲稱通過。

### VAL-004 — Level 3: Unit Tests

驗證局部可測邏輯。修復 Bug 時，合理可行的情況下加入 regression test 或等效測試。

### VAL-005 — Level 4: Integration Tests

驗證 module wiring、config parsing、database initialization、command registration 或其他跨元件互動。

### VAL-006 — Level 5: Smoke Test

驗證最小可用流程，例如啟動、載入主要模組、執行基本操作與正常關閉。

### VAL-007 — Level 6: Real Environment Verification

依賴 Discord、Minecraft、OS、Network API、Hardware 或第三方服務的功能，只有在對應環境實測後才能宣稱完整驗證。

### VAL-008 — Regression 要看受影響的舊路徑

修復或重構後特別檢查 Public API、Import path、Config compatibility、Persistent Data、Startup / Shutdown、Loader / Reload 與受影響的舊功能。

### VAL-009 — 不為了綠燈破壞測試

測試失敗先判斷是否由本次修改造成、是否是既有失敗、或測試本身已過時。不要為了讓 CI 通過就刪除合理測試、放寬 Assertion 或靜默忽略錯誤。

### VAL-010 — 回報要精確

使用「已閱讀、已解析、已編譯、已執行測試、已完成 Smoke test、已實際環境驗證、未執行、無法在目前環境驗證」等精確描述，不用「全部正常」概括未執行的層級。
