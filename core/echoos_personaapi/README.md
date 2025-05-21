
# EchoOS Core Module – echoos_personaapi

This module provides an interface between EchoOS and persona tone modifiers.

---

## 🧠 Purpose

The personaapi injects identity-specific markers into semantic input streams.  
It connects `/persona/` data (tone, memory, behavior) into the semantic pipeline.

---

## ✅ Capabilities

- Loads named persona ID
- Prepends tags or tone modifiers to input text
- Supports modular personalization of all operator calls

---

## 🧪 Example Input

```json
{
  "persona": "EchoSEED-v4",
  "input_text": "search the emotional profile"
}
```

---

## ✅ Output

```json
{
  "persona": "EchoSEED-v4",
  "modified_input": "[EchoSEED-v4] search the emotional profile"
}
```

---

## 📄 Related Files

- `OperatorSpec_echoos_personaapi.md`
- `echoos_personaapi.py`
- `echoos_personaapi.trace.template.jsonl`

---

## 🗂 Directory

`/core/`
