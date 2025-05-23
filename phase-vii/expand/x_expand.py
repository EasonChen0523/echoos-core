def run(input_data):
    text = input_data.get("text", "")
    mode = input_data.get("mode", "")

    expansions = {
        "difficult": "extremely difficult",
        "advanced": "boldly advanced",
        "hesitation": "hesitation and fear",
        "good decision": "very good decision",
        "positive": "highly positive"
    }

    expanded_text = text
    amplified = []

    for key, val in expansions.items():
        if key in expanded_text:
            expanded_text = expanded_text.replace(key, val)
            amplified.append(val.replace(key, "").strip())

    return {
        "expanded_text": expanded_text,
        "amplified_tokens": amplified
    }