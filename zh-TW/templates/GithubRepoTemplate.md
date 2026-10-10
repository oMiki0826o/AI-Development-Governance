# GitHub 專案文件產生器(單檔模板) v1.3.0

> 使用方式: 發布新專案時, 複製本檔案全文貼給 AI, 並提供專案基本資訊.
> AI 依照下方規則, 先問清楚未確認的項目, 再產出對應內容(README.md, LICENSE, .gitignore, Discord 文案, 或僅其中一項).
>
> 標點符號規則: 本模板與所有產出內容一律使用半形標點(, . : ; ? ! ( ) "" -), 禁止使用全形標點(, 。 : ; ? ! ( ) 「」).

---

## 0. 生成前必問清單(AI 執行前必須逐一確認, 不可自行假設或留白)

- 專案名稱, 一句話簡介(中/英各一句)
- 專案類型: 遊戲/創作類(軟體) / 工具/程式庫 / Minecraft 機器/建築作品 / 其他
  - 若為 Minecraft 機器/建築作品, Discord 文案改用第 4.2 節樣式, 且需另外確認三點: 1. 是否仍需要 README/LICENSE/.gitignore(部分作品僅分享檔案, 不一定有程式碼); 2. 「注意事項」區塊需要分為哪些類別(例如: 整體, 輸出端, 輸入端, 或其他自訂分類); 3. 「特點」是否每項都要在下方補一行 `-#` 技術說明(推薦, 呈現較專業), 或僅列關鍵字即可(較簡潔但資訊量低).
- 技術棧(用於徽章與 .gitignore 區塊挑選)
- 主要功能(3~6 點)
- 安裝/執行方式
- 授權條款(預設 MIT, 如需其他請說明是哪一種, 例如 Apache-2.0 / GPL-3.0 / BSD-3-Clause 等)
- **本次要產出的項目(可複選, 不再限定固定組合)**: README / LICENSE / .gitignore / Discord 文案(含 4.1 或 4.2) / GitHub Repo 建議簡述
  - 若只勾選 Discord 文案, 跳過 README/LICENSE/.gitignore, 直接進入第 4 節
  - 若未勾選任何 GitHub 發布相關檔案(README/LICENSE/.gitignore), 不附第 5 節建議簡述
- 雙語呈現優先順序: 中文在前(預設) 或 English 在前(若專案主要面向英文社群)
- 版本標示: 除了"作品版本號"外, 是否有其他需要標示的相容版本(例如 Minecraft 資料包的"遊戲相容版本", Unity/引擎版本, 系統需求版本等), 分別是什麼, 要用什麼標籤文字
- 是否需要"展示 Demo"區塊(並非每個專案都有, 須主動詢問)
- 若上一項為"需要": 是否要嵌入實際展示圖片(使用者習慣上大多附 1~2 張), 需要的話大約幾張, 各自呈現什麼內容, 圖片是放在 repo 內(相對路徑)還是外部連結
- 本專案是否為市面上既有工具/作品的優化版, 整合版, 改版或替代品? 若是, 原工具/原作品名稱是什麼, 主要差異或優勢為何(用於產生對照表)
- 若本次含 Discord 文案且涉及 GitHub 連結: GitHub 帳號與 repo 路徑, 最新版本號與下載檔名, 所有已發布版本號列表(用於 Releases 清單; 若列表超過 5 個版本, 僅列最新 5 個並附 Releases 主頁連結, 不全部列出以免超出 Discord 訊息長度限制)
- 聯絡方式或其他連結(若使用者主動提供才加入, 不主動詢問)

任何欄位不明確時, AI 必須提問確認, 不得用 `[TODO]` 帶過或自行編造內容.

---

## 1. README.md 生成規則

### 1.1 固定結構(不可增減章節順序)

必留: 關於, 功能, 安裝, 使用方式, 授權.
另保留: 徽章, 目錄.
條件保留: 展示 Demo(含或不含實際圖片, 依第 0 節確認), 對照表(僅當專案為既有工具的優化/改版時產生).
不使用: 技術棧表格, Roadmap 勾選清單, 聯絡方式獨立章節(如有聯絡資訊, 併入文件最下方一行, 不獨立成節).

### 1.2 徽章(Badges)

僅使用 Shields.io 純資訊徽章, 不使用 emoji 或裝飾圖示. 基礎徽章固定三種, 另依第 0 節確認的相容版本動態新增, 範例:

```markdown
![Version](https://img.shields.io/badge/version-1.0.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Tech](https://img.shields.io/badge/stack-Unity-lightgrey)
![Minecraft](https://img.shields.io/badge/minecraft-1.21-orange)
```

"相容版本"徽章可依專案性質重複 0~n 個, 每一種都需獨立一枚徽章, 不可與作品版本徽章合併顯示.
若授權非 MIT, License 徽章文字須改為對應 SPDX 縮寫(例如 `Apache-2.0`, `GPL-3.0`), 不可仍寫 MIT.

### 1.3 雙語呈現規則

不逐段中英夾雜. 採"中文 | English"切換連結置頂(或依第 0 節確認的優先順序反過來), 全文分兩區堆疊在同一份檔案.

```markdown
[中文](#中文) | [English](#english)
```

生成後建議實際點擊目錄錨點確認可正確跳轉(GitHub 對中文標題的錨點轉換偶有例外), 若發現跳轉失效, 手動調整錨點文字.

### 1.4 README 骨架(含雙語區域)

```markdown
# {{專案名稱}}

![Version](https://img.shields.io/badge/version-{{作品版本}}-blue)
![License](https://img.shields.io/badge/license-{{授權SPDX縮寫}}-green)
![Tech](https://img.shields.io/badge/stack-{{主要技術}}-lightgrey)
![{{相容項目標籤}}](https://img.shields.io/badge/{{相容項目標籤}}-{{相容版本號}}-orange)

[中文](#中文) | [English](#english)

---

## 中文

### 目錄
- [關於](#關於)
- [功能](#功能)
- [展示-demo](#展示-demo)      <!-- 僅在確認需要時保留此行 -->
- [對照表](#對照表)           <!-- 僅在確認為優化版/改版時保留此行 -->
- [安裝](#安裝)
- [使用方式](#使用方式)
- [授權](#授權)

### 關於
{{專案詳細說明, 中文}}

### 功能
- {{功能項目1}}
- {{功能項目2}}
- {{功能項目3}}

### 展示 Demo
{{截圖/GIF/連結; 僅在確認需要時產生本節. 習慣上放 1~2 張圖片, 使用 ![說明]({{圖片路徑}}) 語法}}

![{{圖片說明1}}]({{圖片路徑1}})
![{{圖片說明2}}]({{圖片路徑2}})

### 對照表
{{僅在確認為既有工具優化版/改版時產生本節}}

| 項目 | {{原工具/原作品名稱}} | {{本專案名稱}} |
| --- | --- | --- |
| {{比較項目1, 如效能}} | {{原版表現}} | {{本專案表現}} |
| {{比較項目2, 如相容性}} | {{原版表現}} | {{本專案表現}} |
| {{比較項目3, 如維護狀態}} | {{原版表現}} | {{本專案表現}} |

### 安裝
\`\`\`bash
{{安裝指令, 依技術棧產生}}
\`\`\`

### 使用方式
\`\`\`bash
{{使用範例}}
\`\`\`

### 授權
本專案採用 {{授權條款}} 授權, 詳見 [LICENSE](./LICENSE).

---

## English

### Table of Contents
- [About](#about)
- [Features](#features)
- [Demo](#demo)          <!-- keep only if confirmed needed -->
- [Comparison](#comparison)   <!-- keep only if this is an optimized/alt version -->
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

### About
{{English description}}

### Features
- {{feature 1}}
- {{feature 2}}
- {{feature 3}}

### Demo
{{screenshots/GIF/links; include only if confirmed needed, usually 1-2 images}}

### Comparison
{{include only if this project is an optimized/alt version of an existing tool}}

| Item | {{Original Tool}} | {{This Project}} |
| --- | --- | --- |
| {{item 1}} | {{original}} | {{this project}} |

### Installation
\`\`\`bash
{{install command}}
\`\`\`

### Usage
\`\`\`bash
{{usage example}}
\`\`\`

### License
This project is licensed under the {{授權條款}} License, see [LICENSE](./LICENSE).
```

---

## 2. LICENSE 生成規則

**MIT(預設)**: 將 `{{YEAR}}`, `{{AUTHOR}}` 替換為當年年份與使用者指定作者/帳號.

```
MIT License

Copyright (c) {{YEAR}} {{AUTHOR}}

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

**其他授權條款(重要修正)**: 若使用者指定 MIT 以外的授權(例如 Apache-2.0, GPL-3.0, BSD-3-Clause, Unlicense 等), AI **不得憑記憶自行默寫或改寫全文**, 必須:
1. 明確告知使用者將使用哪一個 SPDX 標準版本的官方全文.
2. 以該授權在 spdx.org/licenses 或 choosealicense.com 上登載的標準文字為準, 完整呈現條款, 不可省略段落或條件.
3. 同步更新 README 授權章節文字與 License 徽章的 SPDX 縮寫, 兩處必須一致, 不可只改其中一處.

若無法確認官方全文來源, 應向使用者說明並請求提供官方文字, 而非自行編造.

---

## 3. .gitignore 生成規則

依第 0 節確認的技術棧, 從下列區塊挑選組合, 通用區塊一律加入, 區塊間以註解分隔. 只保留與確認技術棧對應的區塊, 不相關區塊一律刪除, 不可整包照抄.

```
# --- 通用/OS/IDE(一律加入) ---
.DS_Store
Thumbs.db
.vscode/
.idea/
*.swp
.env
.env.local
*.log

# --- 專案本地資料與 AI 協作紀錄(一律加入) ---
data/

# --- Unity(若技術棧含 Unity) ---
[Ll]ibrary/
[Tt]emp/
[Oo]bj/
[Bb]uild/
[Bb]uilds/
[Ll]ogs/
[Uu]serSettings/
*.csproj
*.sln
*.pdb

# --- Godot(若技術棧含 Godot) ---
.godot/
.import/
export.cfg
export_presets.cfg

# --- Node.js(若技術棧含 Node.js/前端) ---
node_modules/
npm-debug.log*
dist/
.next/

# --- Python(若技術棧含 Python) ---
__pycache__/
*.pyc
.venv/
venv/
*.egg-info/
.pytest_cache/

# --- Java/Gradle(若技術棧含 Java) ---
.gradle/
build/
*.class
*.jar
!gradle-wrapper.jar

# --- Rust/Cargo(若技術棧含 Rust) ---
target/
Cargo.lock       # 若為函式庫(library)保留追蹤, 若為執行檔(binary)專案則忽略, 依實際情況決定是否列入

# --- Go(若技術棧含 Go) ---
/bin/
/vendor/
*.exe
*.test

# --- Docker(若專案含 Dockerfile/容器化部署) ---
*.env.docker
docker-compose.override.yml
```

---

## 4. Discord 發布文案生成規則

字數 300~500 字(4.2 樣式不受此限, 依原格式彈性調整), 不用 emoji. 此節可獨立產出(第 0 節僅勾選 Discord 文案時), 也可與 README 等一併產出. 依第 0 節確認的專案類型, 選擇 4.1 或 4.2 樣式.

**長度限制提醒**: Discord 單則訊息上限約 2000 字符, 若 Releases 版本列表過長導致超出, 僅列最新 5 個版本, 其餘一律導向 Releases 主頁連結, 不逐條列出全部歷史版本.

### 4.1 一般軟體/工具/遊戲類 Discord 文案

連結區塊固定使用以下結構, 不可更動格式(方括號內文字用反引號包住, 版本下載與各版本 tag 連結一律用 `<>` 包住網址以避免預覽embed, repo 主連結與 Releases 主連結不加 `<>`):

```markdown
**{{專案名稱}}**
{{一句話簡介(中)}}

---

{{2~3 句專案說明, 口語化}}

主要功能:
- {{功能項目1}}
- {{功能項目2}}
- {{功能項目3}}

技術棧: {{`主要技術`, `逗號分隔`}}

- Github 庫: [`{{專案名稱}}`]({{repo 連結}})
- 安裝最新: [`{{最新版本號}}`](<{{最新版本下載連結}}>)
- 全部版本: [`Releases`]({{Releases 主頁連結}})
  - [`{{版本號1}}`](<{{版本1 tag 連結}}>)
  - [`{{版本號2}}`](<{{版本2 tag 連結}}>)
  - [`{{版本號3}}`](<{{版本3 tag 連結}}>)
```

若確認需要展示圖片, 於"主要功能"之後, "技術棧"之前插入 1~2 張圖片(直接貼圖片連結或上傳附件, 不使用 Markdown 圖片語法, 因 Discord 會自動預覽).

### 4.2 Minecraft 機器/建築作品 Discord 文案

沿用使用者慣用格式, 使用 Discord 專屬語法: `>` 引用區塊, `-#` 小字補充, `##` 標題,反引號強調關鍵字, `**粗體**` `*斜體*` 強調重點.

**撰寫品質規範(避免流於鬆散關鍵字堆砌)**:
- 「特點」若第 0 節確認需要 elaboration, 每項下方補一行 `-#` 技術說明, 說明該特點具體帶來什麼能力或效果, 不可只重述關鍵字本身.
- 「注意」每一條一律遵循「**關鍵元件**(粗體) + 具體要求或限制 + 原因/後果」三段式結構, 禁止寫成無因果的空泛提醒(例如禁止只寫"請小心操作", 應寫成"**某元件**必須維持某狀態, 否則會導致某後果").
- 不同「注意」分類之間以空行分隔, 呈現段落層次, 不可全部緊貼在一起.
- `*斜體*` 用於標記先後順序或相對位置關係(如"之前"/"之後"), `**粗體**` 用於標記結構中的關鍵元件名稱, 兩者不可混用於同一強調對象.

```markdown
作者: `{{使用者名稱}}` `<@{{Discord 使用者 ID}}>`
版本: `{{Minecraft 版本}}`
---
> {{標語第一行}}
> {{標語第二行}}
-# {{小字補充說明, 可選}}
---
## 特點:
- `{{特點1}}`
  - -# {{技術說明1, 僅在第 0 節確認需要 elaboration 時產生}}
- `{{特點2}}`
  - -# {{技術說明2}}
- `{{特點3}}`
  - -# {{技術說明3}}

- Github 庫: [`{{專案名稱}}`]({{repo 連結}})
- 安裝最新: [`{{最新版本號}}`](<{{最新版本下載連結}}>)
- 全部版本: [`Releases`]({{Releases 主頁連結}})
  - [`{{版本號1}}`](<{{版本1 tag 連結}}>)
  - [`{{版本號2}}`](<{{版本2 tag 連結}}>)

## 注意:
- {{自訂分類1, 依第 0 節確認需求, 例如 整體}}
  - -# **{{關鍵元件}}** {{具體要求}}, 否則{{後果}}
  - -# **{{關鍵元件}}** {{具體要求}}, 否則{{後果}}

- {{自訂分類2, 依第 0 節確認需求, 例如 輸出端}}
  - -# **{{關鍵元件}}** 必須位於 *{{先後位置}}*, {{原因}}

- {{自訂分類3, 依第 0 節確認需求, 例如 輸入端}}
  - -# **{{關鍵元件}}** {{具體要求}}, {{原因}}
```

分類數量與名稱需在第 0 節與使用者確認後彈性調整. 若此類作品仍有 GitHub repo(例如附結構檔案/schematic), 連結區塊固定插入於 `## 特點:` 與 `## 注意:` 之間, 格式與 4.1 一致(Github 庫, 安裝最新, 全部版本三行), **不可**包含專案名稱, 簡介, 主要功能等 4.1 樣式的多餘元素(除非使用者額外要求); 若無 repo, 則省略此區塊, 直接從 `## 特點:` 接到 `## 注意:`.

---

## 5. GitHub Repo 建議簡述(僅當本次輸出包含 README/LICENSE/.gitignore 等 GitHub 發布內容時附上)

若本次輸出未包含上述任一 GitHub 發布相關檔案(例如僅產出 Discord 文案), 不產生本節.
其餘情況, AI 需額外附上一句可直接貼進 GitHub Repo 設定"About/Description"欄位的建議簡述, 控制在約 50~120 字元內, 中英各一句:

```
建議簡述(中): {{一句話, 含關鍵字, 適合 About 欄位}}
Suggested description (EN): {{one sentence, keyword-friendly, for the About field}}
```

---

## 6. 輸出檢查清單(AI 自我檢查用)

* [ ] 已完成第 0 節所有必問項目確認, 無自行假設欄位
* [ ] 已確認本次輸出範圍(可複選: README/LICENSE/.gitignore/Discord/建議簡述)與專案類型(一般/Minecraft 機器建築作品)
* [ ] 若為 Minecraft 作品, 已確認「注意事項」需要的分類架構, 以及「特點」是否需要 -# 技術說明elaboration
* [ ] 若為 Minecraft 作品, 「注意」每條皆遵循"關鍵元件+要求+後果"三段式結構, 分類間已留空行, 無空泛無因果的提醒句
* [ ] Demo 區塊, 展示圖片, 對照表皆依確認結果決定是否產生, 未經確認一律不產生
* [ ] 版本徽章依專案性質正確拆分(作品版本 + 各相容版本各自一枚), License 徽章文字與實際授權 SPDX 縮寫一致
* [ ] 若授權非 MIT, 已使用官方 SPDX 標準全文, 未自行編造或省略條款
* [ ] 中文區與 English 區皆完整, 結構對稱, 且已依第 0 節確認的語言優先順序排列(若本次有產出 README)
* [ ] .gitignore 僅含實際使用的技術棧區塊
* [ ] Discord 連結區塊格式與範例完全一致(Github 庫/安裝最新/全部版本三行, tag 連結用 `<>` 包住), 版本列表未超過 5 條
* [ ] 若為 Minecraft 作品且包含 repo 連結, 確保未加入專案名稱, 簡介等不必要元素
* [ ] 若本次輸出包含 GitHub 相關檔案, 已附上 GitHub Repo 建議簡述; 若未包含則未附上
* [ ] 全文一律使用半形標點, 無任何全形標點殘留
* [ ] 無任何未替換的 `{{變數}}` 殘留

---

## 7. 注意事項統整(Notes, 所有須留意規則彙整於此)

* 全文一律使用半形標點(, . : ; ? ! ( )), 禁止使用全形標點(全形逗號句號冒號分號問號驚嘆號括號等).
* 未確認欄位一律用提問處理, 禁止用 `[TODO]` 帶過或自行編造.
* Demo, 展示圖片, 對照表三者皆為條件式章節, 各自獨立確認, 互不影響彼此是否產生.
* 版本徽章不可把"作品版本"與"相容版本"合併成一枚, 須依數量各自獨立徽章; License 徽章文字須與實際授權 SPDX 縮寫一致.
* 徽章全面禁用 emoji 與裝飾圖示, 僅用 Shields.io 純資訊樣式.
* 雙語僅用"中文 | English"分區堆疊呈現(或依確認的優先順序反過來), 不逐段中英夾雜.
* .gitignore 只保留實際技術棧對應區塊, 禁止整包照抄未使用的技術區塊.
* 產出範圍改為可複選(README/LICENSE/.gitignore/Discord/建議簡述), 未勾選的項目不產生, 對應項目未包含時不附加建議簡述.
* Discord 連結區塊必須固定使用第 4.1 節格式, tag 與下載連結加 `<>`, repo 主連結與 Releases 主連結不加; 版本列表過長時僅列最新 5 個.
* Minecraft 機器/建築作品類專案, Discord 文案改用第 4.2 節格式, 連結區塊需保持乾淨, 且注意事項分類需動態詢問.
* 4.2 節「注意」每條須為"關鍵元件+具體要求+後果"三段式, 禁止空泛提醒; 分類之間留空行; 「特點」是否加 -# 技術說明依第 0 節確認結果決定.
* GitHub Repo 建議簡述僅在有 GitHub 發布相關輸出時附上, 且需中英各一句, 控制字數.
* LICENSE 預設 MIT, 變更授權時必須採用官方 SPDX 標準全文, 不可自行編造, 且 README 授權章節與徽章文字須同步更新.
