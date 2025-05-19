
# x_enhance_contrast.py
# EchoOS Phase VIII Module: × ENHANCE.CONTRAST
# Amplifies intra-segment semantic contrast by boosting dominant salience

def enhance_contrast(segments):
    enhanced = []
    for seg in segments:
        text = seg.get("text", "")
        words = text.split()
        tone = seg.get("tone_vector", [0.5] * len(words))
        salience = seg.get("salience_vector", [0.5] * len(words))

        high = [w for i, w in enumerate(words) if salience[i] > 0.7]
        low = [w for i, w in enumerate(words) if salience[i] < 0.3]

        modified = " ".join(w for w in words if w not in low)

        enhanced.append({
            "id": seg["id"],
            "contrast_highlight": high,
            "suppressed": low,
            "modified_text": modified
        })
    return enhanced
