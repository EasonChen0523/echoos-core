# OperatorSpec_echoos_shrink.md

## 運算元名稱
× SHRINK

## 語義階段
Phase VII

## 模組功能
針對輸入語段進行語義壓縮：
- 減少語氣干擾
- 去除風格性贅詞與低語義權重詞彙
- 保留語段主幹 × 突出焦點語義

## 演算法概念
- 使用 SentenceTransformer (MiniLM-L6-v2)
- 依語義相似度移除保留意義貢獻度低的詞彙
- 模擬語義壓縮，返回 shrink_score 與剔除片段

## 輸入格式
```json
{
  "text": "She seemed somewhat uncertain, possibly due to fear or indecision.",
  "mode": "semantic_weight"
}
```

## 輸出格式
```json
{
  "compressed_text": "She somewhat possibly fear",
  "removed_segments": ["seemed", "uncertain,", "due", "to", "or", "indecision."],
  "shrink_score": 0.5
}
```

## 調用建議
適用於語句去風格化處理、模組語義稀疏化、語義骨架抽取等前處理任務。