
# EchoOS Core Module – echoos_promptsystem

This module handles system-level prompt pre-processing and formatting in the EchoOS runtime.

---

## 🧠 Purpose

The promptsystem acts as a gateway between raw user input and semantic operator modules.  
It injects structural hints, semantic mode tags, and prepares the prompt for modulation or execution.

---

## ✅ Capabilities

- Wraps input text with system-level semantic tags
- Supports mode-based formatting (e.g. "brief", "formal")
- Optionally injects pre-context for trace routing

---

## 🧪 Example Input

```json
{
  "text": "summarize the conversation",
  "mode": "brief"
}
```

---

## ✅ Output

```json
{
  "transformed": "[SYSTEM:MODE=brief]\nsummarize the conversation"
}
```

---

## 📄 Related Files

- `OperatorSpec_echoos_promptsystem.md`
- `echoos_promptsystem.py`
- `echoos_promptsystem.trace.template.jsonl`

---

## 🗂 Directory

`/core/`
