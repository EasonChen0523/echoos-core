
# OperatorSpec_×_SEGMENT.md

## Archive Time:
2025/05/18 22:00 (Asia/Taipei)

## Context:
context_digest: EchoOS_construction_2025_05_18
source_origin: Felis Origin Reboot
semantic_shift_type: Structural enhancement

---

## Operator Name:
× SEGMENT

## Phase:
Phase VII – Semantic segmentation × narrative decomposition

---

## Module Functionality:

- Divide a long narrative into smaller, semantically coherent chunks
- Align subsegments based on tonal shifts and linguistic markers
- Support downstream operators like × SMOOTH, × PROJECT(N)

---

## Input Format:
A single segment dictionary:
- `id`: Segment ID
- `text`: Narrative paragraph
- `tone_vector`: Tonal intensity series (float list)

---

## Output Format (SegmentedUnits):
```json
[
  {
    "unit_id": "s_005-1",
    "text": "He looked around slowly.",
    "segment_rank": 1,
    "reason": "punctuation"
  },
  {
    "unit_id": "s_005-2",
    "text": "Everyone was waiting for him to speak.",
    "segment_rank": 2,
    "reason": "intonation continuity"
  }
]
```

---

## Implementation Path:
`/phase-vii/segment/x_segment.py`
