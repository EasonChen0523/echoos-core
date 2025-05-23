# Operator_x_clean.md

## 運算元名稱
× CLEAN

## 語義階段
Phase VII

## 模組功能
移除語段中雜訊、過度修飾語與突兀情緒峰值，用以平滑語義主幹與情緒流。

## 類比影像行為
- 類比影像處理中的 Opening 操作（先 Erode 再 Dilate）
- 對語句進行情緒突起點過濾與主幹語義還原

## 輸入格式
```json
{
  "text": "Clearly, the absolutely amazing result was truly unexpected!",
  "mode": "clean_emotion"
}
```

## 輸出格式
```json
{
  "cleaned_text": "the result was unexpected",
  "removed_noise": ["Clearly", "absolutely", "amazing", "truly"]
}
```

## 調用建議
適用於語句前處理、語氣格式統整、強情緒語段過濾等應用場景，通常接續 × SHRINK、先於 × TRACE FLOW 使用。