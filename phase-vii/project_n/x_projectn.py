
# x_projectn.py
# EchoOS Phase VII Module: × PROJECT(N)
# Project tone vectors into N-dimensional semantic coordinate space

def project_to_nd(segments, dims=["tone", "time"]):
    results = []
    for i, seg in enumerate(segments):
        tone = round(sum(seg.get("tone_vector", [])) / max(1, len(seg["tone_vector"])), 3)
        time = i / len(segments)
        projected = [tone, round(time, 3)] if "time" in dims else [tone]
        results.append({
            "id": seg["id"],
            "projected": projected,
            "dimensions": dims,
            "note": "projected tone-time coordinate"
        })
    return results
