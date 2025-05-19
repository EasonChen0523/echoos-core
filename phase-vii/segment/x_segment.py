
# x_segment.py
# EchoOS Phase VII Module: × SEGMENT
# Splits narrative text into semantically coherent sub-units

import re

def segment_paragraph(entry):
    text = entry.get("text", "")
    tone_vector = entry.get("tone_vector", [])
    sentences = re.split(r'(?<=[.!?])\s+', text)
    segmented = []
    for i, sentence in enumerate(sentences):
        segmented.append({
            "unit_id": f"{entry.get('id')}-{i+1}",
            "text": sentence.strip(),
            "segment_rank": i + 1,
            "reason": "punctuation"
        })
    return segmented
