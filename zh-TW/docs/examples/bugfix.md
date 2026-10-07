# 範例：Bug 修了兩次還是回來

假設一個背景 Task 偶爾重複啟動。第一次直覺是在啟動前多加一個 `if running`；問題仍然出現後，第二次又在另一個入口加一個 lock。這時候如果繼續在第三個地方補 guard，很可能已經進入 `CONV-002` 的 Patch Chain。

比較好的做法是先停下來，把「誰能建立 Task、誰負責關閉、Reload 時舊 Task 在哪裡被取消」畫成簡單的生命週期。也許真正的問題不是缺少第三個 guard，而是 unload 根本沒有 await cancellation，或 extension 被註冊了兩次。

這就是 Stop-and-Reassess 的用途：它不是「遇到困難就放棄」，而是避免在沒有新證據時一直改同一批程式。重建 call chain / resource lifecycle 後，再提出一個可以被驗證的原因，例如「reload 後舊 listener 還存在」。先用 log 或最小測試證明這件事，再動手修。

最後的修復如果讓原本兩個 workaround 都可以刪掉，通常比新增第三層防護更健康。
