def run(input_data):
    text = input_data.get("text", "")
    mode = input_data.get("mode", "")
    candidates = ["REALLY", "hate", "absolutely", "STUNNING"]

    highlights = [w for w in text.replace("!", "").split() if w in candidates]
    score = min(1.0, 0.6 + 0.1 * len(highlights))

    return {
        "highlighted_segments": highlights,
        "emphasis_score": round(score, 2)
    }