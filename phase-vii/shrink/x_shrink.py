from sentence_transformers import SentenceTransformer, util

# 初始化語義模型（建議部署時初始化移至全域）
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

def run(input_data):
    text = input_data.get("text", "")
    mode = input_data.get("mode", "")

    if not text:
        return {"error": "Empty input text."}

    words = text.split()
    original_embedding = model.encode(text, convert_to_tensor=True)

    compressed_words = []
    removed_words = []

    for i, word in enumerate(words):
        modified = words[:i] + words[i+1:]
        modified_text = " ".join(modified)
        modified_embedding = model.encode(modified_text, convert_to_tensor=True)

        similarity = float(util.cos_sim(original_embedding, modified_embedding)[0][0])

        if similarity > 0.92:
            removed_words.append(word)
        else:
            compressed_words.append(word)

    compressed_text = " ".join(compressed_words)
    shrink_score = round(1 - len(compressed_words) / max(len(words), 1), 2)

    return {
        "compressed_text": compressed_text,
        "removed_segments": removed_words,
        "shrink_score": shrink_score
    }