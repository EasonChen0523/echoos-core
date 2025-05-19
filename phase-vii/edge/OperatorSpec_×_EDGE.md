
# OperatorSpec_×_EDGE.md

## Archive Time:
2025/05/18 21:30 (Asia/Taipei)

## Context:
context_digest: EchoOS_construction_2025_05_18
source_origin: Felis Origin Reboot
semantic_shift_type: No shift (semantically consistent)

---

## Operator Name:
× EDGE

## Phase:
Phase VII – Semantic boundary detection × tonal transition analysis

---

## Module Functionality:

- Detect abrupt tonal intensity shifts (Tone Gradient)
- Mark conceptual or structural transitions within segments (EdgeBlock)
- Provides cutting points for `× SEGMENT`, `× FUSE`, `× TRACE FLOW`
- Serves as a preprocessing layer for `.trace.jsonl`

---

## Input Format:
List of segment objects containing:
- `id`: Segment ID
- `text`: Original text
- `tone_vector`: List of tone intensity values (float)

---

## Output Format (EdgeBlock):
```json
{
  "segment_id": "s_002",
  "text": "However, he paused briefly, then suddenly mentioned something he had never said before.",
  "is_edge": true,
  "tone_gradient": 0.87,
  "triggered_modules": ["× SEGMENT", "× FUSE"],
  "edge_type": "conceptual_shift",
  "position": 2
}
```

---

## Implementation Path:
`/phase-vii/edge/x_edge.py`
