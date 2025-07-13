# × VERIFY.MULTI – Offline Multi-Model Verifier

Runs the same **trace JSONL** through any number of `llama-cli` GGUF models,  
optionally measures response similarity, and writes the results back to
`*.jsonl`.

---

## ✨ 2025-07 update

| Change | Details |
| ------ | ------- |
| **Central model map** | `models/model_paths.json` stores *model-key → file path* |
| **New flag** `--ngl` | Maps to `llama-cli --gpu-layers` (CUDA/Metal off-load) |
| **No chat hang-ups** | `-no-cnv` is injected automatically to skip interactive mode |
| **Gemma 3-4B-it support** | Tested with `Q4_K_M` (≈ 2.3 GiB, 5-7 tok/s on RTX 4060) |

---

## Installation

```bash
pip install -r requirements.txt          # tqdm + sentencepiece
# For similarity scoring (optional)
pip install sentence-transformers
