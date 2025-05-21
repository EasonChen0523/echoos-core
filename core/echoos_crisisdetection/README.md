
# EchoOS Core Module – echoos_crisisdetection

This module detects high-volatility tone patterns or semantic anomalies.

---

## 🧠 Purpose

To identify emotional breakdowns, erratic tone sequences, or structural instability in trace input.  
Useful for critical alerting, fallback initiation, or semantic signal diagnosis.

---

## ✅ Capabilities

- Detects abrupt tone vector changes
- Flags volatile segments for semantic inspection
- Supports recovery triggering and future alert pipelines

---

## 🧪 Example Input

```json
{
  "trace": [
    {"id": "s_010", "tone_vector": [0.1, 0.95, 0.15]},
    {"id": "s_011", "tone_vector": [0.9, 0.2, 0.85]}
  ]
}
```

---

## ✅ Output

```json
{
  "status": "crisis_detected",
  "crisis_ids": ["s_010", "s_011"]
}
```

---

## 📄 Related Files

- `OperatorSpec_echoos_crisisdetection.md`
- `echoos_crisisdetection.py`
- `echoos_crisisdetection.trace.template.jsonl`

---

## 🗂 Directory

`/core/`
