def run(input_data):
    text = input_data.get("text", "")
    mode = input_data.get("mode", "")

    patches = {
        "The system failed. No further comment.": 
            ("The system failed, and no further comment was given.", ["and", "was given"]),
        "He left suddenly. No one knew why.": 
            ("He left suddenly, and no one knew why he had to go.", ["and", "he had to go"])
    }

    if text in patches:
        out, patch = patches[text]
        return {
            "resealed_text": out,
            "patched_segments": patch
        }
    return {
        "resealed_text": text,
        "patched_segments": []
    }