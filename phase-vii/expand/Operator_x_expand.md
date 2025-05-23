# Operator_x_expand.md

## 運算元名稱
× EXPAND

## 語義階段
Phase VII

## 模組功能
針對語段中主幹語義與情緒節點進行「語義擴張」處理，強化關鍵概念的語氣張力與風格密度。

## 語義行為
- 類比影像形態學中的 Dilation 擴張
- 放大概念性詞彙與其語境關聯字詞
- 適用於文本強化、敘事焦點清晰化

## 輸入格式
```json
{
  "text": "The mission was difficult, yet they advanced without hesitation.",
  "mode": "semantic_expand"
}
```

## 輸出格式
```json
{
  "expanded_text": "The mission was extremely difficult, yet they boldly advanced without hesitation and fear.",
  "amplified_tokens": ["extremely", "boldly", "fear"]
}
```

## 調用建議
可搭配 × SHRINK 形成收斂－擴張語義處理組合，用於敘事對比強化、關鍵語段情緒建構等任務。