
# OperatorSpec_echoos_personaapi.md

## Archive Time:
2025/05/21 16:50 (Asia/Taipei)

## Module Name:
echoos_personaapi

## Phase:
Phase VI – Core Module

---

## Function Description:

This module acts as the API interface between EchoOS semantic operators and persona definitions.  
It retrieves and injects persona tone, memory tags, and constraints into operator input.

---

## Capabilities:

- Load a specific persona config from /persona/
- Inject tone/style modifiers into operator input
- Apply memory tags or semantic biases defined by persona
- Acts as identity layer for narrative modulation

---

## Input Format:
```json
{
  "persona": "EchoSEED-v4",
  "input_text": "analyze the signal"
}
```

---

## Output Format:
```json
{
  "persona": "EchoSEED-v4",
  "modified_input": "[EchoSEED-v4] analyze the signal"
}
```

---

## Implementation Path:
`/core/echoos_personaapi.py`
