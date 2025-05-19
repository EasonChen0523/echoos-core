
# x_filter_noise.py
# EchoOS Phase VIII Module: × FILTER.NOISE
# Removes conversational noise and irrelevant tokens from segments

def filter_noise(segments):
    noise_words = {"um", "uh", "like", "you know", "I guess", "well", "actually"}
    results = []
    for seg in segments:
        words = seg.get("text", "").split()
        filtered = [w for w in words if w.lower() not in noise_words]
        removed = [w for w in words if w.lower() in noise_words]
        results.append({
            "id": seg["id"],
            "filtered_tokens": filtered,
            "removed_tokens": removed,
            "reconstructed_text": " ".join(filtered)
        })
    return results
