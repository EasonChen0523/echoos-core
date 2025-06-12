# × VERIFY.MULTI – EchoOS Phase X

> **Run one prompt set through multiple local LLM models and check consistency**

---

## Features

* CLI wrapper around **`llama-cli`** for batch inference
* Supports **any number of `.gguf` models** in one run
* Logs per-model JSON, plus a `results.jsonl` summary
* Built-in similarity metrics  
  * **Jaccard token overlap** (always on)  
  * **FH-score** (embedding cosine – optional, needs `sentence-transformers`)
* Windows / Linux tested, Python ≥ 3.10

## Quick start

```bash
# ① install deps
python -m pip install -r requirements.txt

# ② run
python verify_multi.py \
  --input   ../../traces/dev/trace_smoke.jsonl \
  --models  D:/models/llama/llama-2-7b.Q4_K_M.gguf \
            D:/models/llama/gemma-2b.Q4_K_M.gguf \
  --llama-cli "D:/models/llama-bin/llama-cli.exe" \
  --n-tokens 128 --temp 0.7 \
  --output  ../../results/dev_run

If your llama-cli < b5500, use --skip-json or upgrade to get structured output.

#3 update
Old version llama-cli→stderr Merge、build-in filtering noise