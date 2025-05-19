
# x_edge.py
# EchoOS Phase VII Module: × EDGE
# Semantic module: tonal shift detector × conceptual boundary marker

def detect_edges(trace):
    edge_blocks = []
    for i, segment in enumerate(trace):
        tone_vector = segment.get("tone_vector", [])
        gradient = sum(abs(tone_vector[j+1] - tone_vector[j]) for j in range(len(tone_vector)-1)) / max(len(tone_vector)-1, 1) if tone_vector else 0
        edge_triggered = gradient > 0.65 or any(k in segment.get("text", "").lower() for k in ["but", "however", "suddenly"])
        edge_blocks.append({
            "segment_id": segment.get("id", f"s_{i:03}"),
            "text": segment.get("text", ""),
            "is_edge": edge_triggered,
            "tone_gradient": round(gradient, 4),
            "triggered_modules": ["× SEGMENT", "× FUSE"] if edge_triggered else [],
            "edge_type": "conceptual_shift" if edge_triggered else "none",
            "position": i
        })
    return edge_blocks
