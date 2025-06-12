#!/usr/bin/env python3
"""
EchoOS Phase X – × VERIFY.MULTI

A utility for running the same prompt set through multiple local LLM models
(via `llama-cli`) and collecting comparable responses + basic metrics that can
feed back into EchoOS trace validation.

Usage (minimal):
    python verify_multi.py \
        --input trace_en_003.jsonl \
        --models models/llama-2-7b.Q4_K_M.gguf \
                 models/gemma-2b.Q4_K_M.gguf \
        --llama-cli D:/models/llama-bin/llama-cli.exe

Outputs a folder `verify_multi_out/` (default) that contains one combined
`results.jsonl` file and per‑model raw response files.

Designed to run on Windows 11 (PowerShell / CMD) and Linux shells alike.

★ Features
• Streams prompts to each model sequentially (can be extended to parallel).
• Captures wall‑clock latency for each generation.
• Writes compact JSONL: {id, model, response, latency_ms, ts}.
• Includes `--compare-similarity` flag that measures cosine similarity of
  Sentence‑BERT embeddings between model outputs for quick consistency check
  (optional; requires `pip install sentence-transformers`).
• Graceful CTRL+C handling – partial results are flushed before exit.

This file is **self‑contained** and avoids non‑std lib deps unless the optional
similarity mode is turned on.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import time
import datetime as dt
from pathlib import Path
from typing import List, Dict, Any

try:
    from sentence_transformers import SentenceTransformer, util  # optional
except ImportError:
    SentenceTransformer = None  # type: ignore


def run_cli(llama_cli: str, model: Path, prompt: str, n_tokens: int = 256, temp: float = 0.7) -> str:
    """Invoke llama-cli and return the raw stdout string (stripped)."""
    cmd = [
        str(llama_cli),
        "-m", str(model),
        "-p", prompt,
        "-n", str(n_tokens),
        "--temp", str(temp),
        "--no-display-prompt",
    ]

    completed = subprocess.run(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,   # <<< Merge stderr to stdout
        text=True,
        encoding="utf-8",     # <<<< Foreced to use UTF-8
        errors="replace",     # Or "ignore"；Avoid throw
        check=False,
    )

    out = completed.stdout

    # ----- filtering noise, keep true response -----
    text_lines = [
        ln.strip()
        for ln in out.splitlines()
        if ln and not ln.startswith(("ggml_", "llama_", "build:", "load:", "print_info:", "sampler ", "system_info:"))
    ]

    CUTOFF = "generate:"
    pos = out.rfind(CUTOFF)
    if pos != -1:
        # Extract all raws after raw of "generate:"
        tail_lines = out[pos:].splitlines()[1:]     # <— [1:] Skip first raw
    else:
        tail_lines = out.splitlines()

    text_lines = [
        ln.strip()
        for ln in tail_lines
        if ln and not ln.startswith(("llama_perf_", "llama_perf", "sampler ", "llama_context:"))
    ]

    response = " ".join(text_lines).strip()


    if completed.returncode != 0 and not response:
        raise RuntimeError(f"llama-cli failed: {out[:300]}")

    return response or "<empty>"



def embed_texts(texts: List[str]) -> List[Any]:
    if SentenceTransformer is None:
        raise ModuleNotFoundError("sentence-transformers not installed; run `pip install sentence-transformers` or omit --compare-similarity.")
    model = SentenceTransformer("all-MiniLM-L6-v2")
    return model.encode(texts, convert_to_tensor=True, normalize_embeddings=True)  # type: ignore


def similarity_score(a: str, b: str) -> float:
    emb_a, emb_b = embed_texts([a, b])
    return float(util.cos_sim(emb_a, emb_b))  # type: ignore


def process_sample(sample: Dict[str, Any], models: List[Path], args) -> List[Dict[str, Any]]:
    out: List[Dict[str, Any]] = []
    for model_path in models:
        ts0 = time.perf_counter()
        resp = run_cli(args.llama_cli, model_path, sample["prompt"], n_tokens=args.n, temp=args.temp)
        latency_ms = (time.perf_counter() - ts0) * 1000.0
        record = {
            "id": sample["id"],
            "model": model_path.name,
            "response": resp,
            "latency_ms": round(latency_ms, 1),
            "timestamp": dt.datetime.utcnow().isoformat() + "Z",
        }
        out.append(record)
    # optional similarity between first two models
    if args.compare_similarity and len(out) >= 2:
        out[0]["sim_to_next"] = similarity_score(out[0]["response"], out[1]["response"])
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description="Verify consistency across multiple local LLMs via llama-cli")
    ap.add_argument("--input", required=True, help="JSONL file with fields {id, prompt}")
    ap.add_argument("--models", nargs="+", required=True, help="One or more GGUF model paths")
    ap.add_argument("--llama-cli", required=True, help="Path to llama-cli executable")
    ap.add_argument("--output", default="verify_multi_out", help="Output directory")
    ap.add_argument("-n", type=int, default=256, help="Max tokens to generate per model")
    ap.add_argument("--temp", type=float, default=0.7, help="Sampling temperature")
    ap.add_argument("--compare-similarity", action="store_true", help="Compute cosine similarity between first two model outputs (needs sentence-transformers)")
    args = ap.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        raise FileNotFoundError(input_path)

    models = [Path(m) for m in args.models]
    for m in models:
        if not m.exists():
            raise FileNotFoundError(m)

    out_dir = Path(args.output)
    out_dir.mkdir(parents=True, exist_ok=True)
    combined_path = out_dir / "results.jsonl"

    with combined_path.open("w", encoding="utf-8-sig") as combined_out:
        for line in input_path.read_text(encoding="utf-8-sig").splitlines():
            if not line.strip():
                continue
            sample = json.loads(line)
            try:
                records = process_sample(sample, models, args)
                for rec in records:
                    combined_out.write(json.dumps(rec, ensure_ascii=False) + "\n")
                    # Also write per-model raw output if needed
                    model_file = out_dir / f"{rec['model']}.jsonl"
                    with model_file.open("a", encoding="utf-8-sig") as mf:
                        mf.write(json.dumps(rec, ensure_ascii=False) + "\n")
            except KeyboardInterrupt:
                print("Interrupted, saving partial results…")
                break

    print(f"Done. Results saved under {out_dir}/")


if __name__ == "__main__":
    main()
