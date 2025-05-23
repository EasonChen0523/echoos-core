# Operator_x_highlight.md

## 運算元名稱
× HIGHLIGHT

## 語義階段
Phase VII

## 模組功能
擷取語段中出現的情緒尖峰、高語氣強度片段或關鍵語氣轉折點。

## 類比影像行為
- 類比影像處理中的 Top Hat 運算
- 對比語義主幹抽取前後，保留突起區作為強化語氣觀察區

## 輸入格式
```json
{
  "text": "I really, REALLY hate when this happens!",
  "mode": "highlight_peak"
}
```

## 輸出格式
```json
{
  "highlighted_segments": ["REALLY", "hate"],
  "emphasis_score": 0.86
}
```

## 調用建議
可搭配 × CLEAN / × TRACE FLOW，作為高情緒輸出區偵測與敘事張力圖之建立基礎模組。