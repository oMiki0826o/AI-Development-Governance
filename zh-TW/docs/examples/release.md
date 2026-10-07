# 範例：從完成修改到發布 ZIP

Release 最容易出錯的地方，是把「原始碼測試成功」直接等同「打包後可以交付」。實際流程可以很簡單，但要分成兩個階段。

先在 Source tree 跑適用的測試與 regression 檢查，確認 README、設定範例與版本資訊已同步。再看 Git 狀態，確認沒有 `.env`、Local DB、Log 或其他本機產物混進來。

接著建立 ZIP。打包完成後重新列一次 ZIP 內容、實際解壓到乾淨暫存目錄，確認必要檔案存在，而且使用者照 README 的最小步驟可以開始使用。這一步是在驗證 Artifact，不是重複驗證 Source tree。

如果專案沒有任何第三方 dependency，就不需要為了 Pre-release Gate 硬做一個空 `requirements.txt`。Gate 關心的是「有依賴時有沒有把它管理好」，而不是每個專案都必須長得一樣。

最後才是 Tag / GitHub Release。這些會改變遠端狀態，因此是否可直接執行仍依專案授權與 `DEC-004` 的邊界決定。
