
# OperatorSpec_×_TRACE_FLOW.md

## Archive Time:
2025/05/18 22:15 (Asia/Taipei)

## Context:
context_digest: EchoOS_construction_2025_05_18
source_origin: Felis Origin Reboot
semantic_shift_type: Functional extension

---

## Operator Name:
× TRACE FLOW

## Phase:
Phase VII – Emotional force tracking × tension propagation visualization

---

## Module Functionality:

- Trace the propagation of semantic tone shifts across segments
- Quantify tension gradients and directionality in narrative sequences
- Output flow vectors for visualization or further projection

---

## Input Format:
Ordered list of segments:
- `id`: Segment ID
- `text`: Segment content
- `tone_vector`: List of float values (emotion intensity)

---

## Output Format (FlowMap):
```json
[
  {
    "from": "s_007",
    "to": "s_008",
    "tension_shift": 0.3,
    "flow_vector": [+0.3],
    "direction": "rising"
  }
]
```

---

## Implementation Path:
`/phase-vii/trace_flow/x_trace_flow.py`
