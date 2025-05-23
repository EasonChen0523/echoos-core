def run(input_data):
    text = input_data.get("text", "")
    mode = input_data.get("mode", "")
    noise = ["Clearly", "absolutely", "amazing", "truly", "Honestly", "just", "pretty", "nothing", "more"]

    words = text.split()
    cleaned = [w for w in words if w.strip(",.!") not in noise]
    removed = [w for w in words if w.strip(",.!") in noise]

    return {
        "cleaned_text": " ".join(cleaned),
        "removed_noise": removed
    }