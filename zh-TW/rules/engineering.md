# Engineering Policy

### ENG-001 — 修改前追蹤相關範圍

先閱讀與任務直接相關的入口、caller、callee、config、tests 與資料流，並確認是否會影響 Public API、Persistent Data、Configuration 或 Resource Lifecycle。

### ENG-002 — 架構調整需要實際理由

優先使用現有合理抽象。不因另一種架構看起來更漂亮就重構；只有需求需要、現有設計直接造成問題，或維護成本已明顯不合理時才擴大架構修改。

### ENG-003 — 正確性與簡單性優先

程式碼依序重視 Correctness、Maintainability、Simplicity、Readability、必要的 Compatibility，以及有實際價值的 Performance。避免 Duplicate Logic、Dead Code、Giant Functions、Hidden Side Effects、Unnecessary Nesting 與 Premature Abstraction。

### ENG-004 — Hard-code 只在真正需要抽離時處理

Secrets、環境差異、可變政策與重複使用的業務設定不應散落硬編碼；演算法固有、局部且意義清楚的 literal 不需要為形式抽出。

### ENG-005 — 錯誤要在合適層級處理

不靜默吞掉重要 Exception。Broad exception 必須有具體理由並搭配 Logging、Recovery、Wrapping 或 Re-raise。Fallback 只有在行為可以明確定義時才使用，不能用來遮住真正錯誤。

### ENG-006 — 設定與秘密分離

環境差異與可調政策集中管理；API Key、Token、Credential 與其他 Secrets 使用環境變數或專案既有 Secret store，不寫進原始碼或公開設定。

### ENG-007 — 新依賴先確認必要性

加入第三方 dependency 前先看標準函式庫或現有依賴能否完成。新增、移除或升級依賴時同步正式 dependency 定義，重大版本升級先評估 breaking change。

### ENG-008 — Resource Lifecycle 必須完整

Thread、Task、Process、Socket、Database connection、HTTP session、File handle 與 FFmpeg 等資源需有可預期的建立、使用與釋放流程。Reload / Unload 不應留下 duplicate listener、背景 task 或 zombie process。

### ENG-009 — Refactor 不能偷偷改行為

重構前先理解目前行為與 call sites；除非任務本身要求，應保留原本對外行為。大型重構與無關功能修改分開，完成後做 regression 檢查。
