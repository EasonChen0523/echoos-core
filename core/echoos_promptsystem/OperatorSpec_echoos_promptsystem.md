
# OperatorSpec_echoos_promptsystem.md

## Archive Time:
2025/05/21 16:20 (Asia/Taipei)

## Module Name:
echoos_promptsystem

## Phase:
Phase VI – Core Module

---

## Function Description:

This module manages system-level prompt pre-processing and enhancement strategies.  
It operates at the boundary between raw input and semantic operator execution,  
injecting structural cues, default context, or tone scaffolding.

---

## Capabilities:

- Applies system-wide prompt transformations
- Adds semantic scaffolding based on tone or scenario
- Embeds implicit trace context to operator input
- Prepares prompt for higher-phase modulation

---

## Input Format:
```json
{
  "text": "please generate a summary of the segment",
  "mode": "formal"
}
```

---

## Output Format:
```json
{
  "transformed": "[SYSTEM:MODE=formal]
please generate a summary of the segment"
}
```

---

## Implementation Path:
`/core/echoos_promptsystem.py`
