
# EchoOS Core Module – echoos_modchain

This module handles modular chaining logic in EchoOS.

---

## 🧠 Purpose

The modchain module allows chaining of multiple semantic operators in a sequence.  
Each operator is executed in turn, passing output to the next. This enables the construction of modular execution flows and multi-stage semantic processing.

---

## ✅ Capabilities

- Loads a list of semantic operator steps
- Simulates execution chaining of multiple modules
- Logs execution path (future: add conditional branching)

---

## 🧪 Example Input

```json
{
  "chain": [
    {"op": "× FILTER.NOISE", "trace_path": "step1.jsonl"},
    {"op": "× EDGE", "trace_path": "step2.jsonl"}
  ]
}
```

---

## ✅ Output

```json
{
  "status": "executed",
  "executed_steps": 2,
  "log": [
    "[EXECUTED] × FILTER.NOISE on step1.jsonl",
    "[EXECUTED] × EDGE on step2.jsonl"
  ]
}
```

---

## 📄 Related Files

- `OperatorSpec_echoos_modchain.md`
- `echoos_modchain.py`
- `echoos_modchain.trace.template.jsonl`

---

## 🗂 Directory

`/core/`
