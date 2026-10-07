# README Template Policy

README 預設保留：專案名稱、資訊徽章、目錄、關於、功能、安裝、使用方式與授權。Demo 與對照表只有在真的適用時才加入。

## Badges

使用 Shields.io 純資訊徽章，不用 Emoji 或裝飾圖示。基本資訊通常包含 Version、License、主要技術；相容版本依專案需要各自獨立一枚，不與作品版本混在一起。

## 雙語

需要雙語時，以完整中文區與完整 English 區呈現，不逐句混雜。預設中文在前；主要面向英文社群時可反轉。

## 建議骨架

```markdown
# <Project Name>

![Version](https://img.shields.io/badge/version-<version>-blue)
![License](https://img.shields.io/badge/license-<SPDX>-green)
![Tech](https://img.shields.io/badge/stack-<tech>-lightgrey)

[中文](#中文) | [English](#english)

---

## 中文

### 目錄
- [關於](#關於)
- [功能](#功能)
- [安裝](#安裝)
- [使用方式](#使用方式)
- [授權](#授權)

### 關於
<實際專案說明>

### 功能
- <feature>

### 安裝
```bash
<real install command>
```

### 使用方式
```bash
<real usage example>
```

### 授權
本專案採用 <License> 授權，詳見 [LICENSE](./LICENSE)。
```

English 區使用相同資訊結構即可。若專案沒有版本制度、Demo、Comparison 或特定相容版本，不為了模板完整度硬加。
