
# x_fuse.py
# EchoOS Phase VII Module: × FUSE(mesh)
# Semantic fusion of multiple segments into a continuous tone mesh

def fuse_segments(segments):
    mesh = []
    current = []
    for seg in segments:
        if not current:
            current.append(seg)
        else:
            diff = abs(current[-1]["tone_vector"][-1] - seg["tone_vector"][0])
            if diff < 0.2:
                current.append(seg)
            else:
                if len(current) > 1:
                    mesh.append(build_mesh(current))
                current = [seg]
    if len(current) > 1:
        mesh.append(build_mesh(current))
    return mesh

def build_mesh(segment_list):
    merged_text = " ".join(s["text"] for s in segment_list)
    avg_quality = sum(abs(s["tone_vector"][0] - s["tone_vector"][-1]) for s in segment_list) / len(segment_list)
    return {
        "mesh_id": f"msh_{segment_list[0]['id'][-1]}",
        "segments": [s["id"] for s in segment_list],
        "merged_text": merged_text,
        "mesh_quality": round(1 - avg_quality, 2),
        "fusion_strategy": "tone-continuity",
        "trace_origin": [s["id"] for s in segment_list]
    }
