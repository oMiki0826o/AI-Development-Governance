# Convergence and Failure Loop Policy

這組規則用來防止問題修著修著變成新的架構負擔。真正的目標不是「試更多方案」，而是在沒有新證據時知道什麼時候該停下來重新理解問題。

### CONV-001 — 新抽象要降低整體複雜度

新增抽象前確認它有穩定責任，而且能減少重複、耦合或不清楚的邊界。單一 Bug 很難修，不足以成為增加 Manager、Adapter、Wrapper 或 Compatibility Layer 的理由。

### CONV-002 — 偵測 Patch Chain

如果 Patch A 為了能工作又要求 Patch B，而 B 又需要 Patch C 或新的 workaround，應重新檢查 Patch A 的方向，而不是把補丁數量當成進度。

### CONV-003 — Failure Loop 觸發 Stop-and-Reassess

以下任一狀況出現時，停止繼續加 Patch：同一核心問題經過兩個實質不同的修正仍重現；A 修好後出現 B、B 修好又使 A 回來；同一批檔案反覆修改與回退但沒有新證據；workaround 持續增加；或對 call chain / data flow / runtime state 的判斷主要依賴猜測。

Stop-and-Reassess 時重新取得完整錯誤與狀態，整理已嘗試方案，標記哪些假設已被證實或否定，重建 call chain / data flow / resource lifecycle，縮小可重現案例，再驗證新的 root-cause 假設。

### CONV-004 — 使用 Complexity Budget

較大的修改完成後，檢查新增了多少概念、每一層是否有獨立責任、是否與既有機制重疊，以及能不能移除舊 workaround。若複雜度增加明顯但可靠性、可測試性或維護性沒有對應收益，應回到較簡單方案。
