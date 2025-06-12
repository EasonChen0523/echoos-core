
# batch_dispatcher.py
# EchoOS Phase IX – Dispatch all batch_input traces based on module naming

import os
import json
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1] / "scheduler"))
from EchoKernelScheduler import EchoKernelScheduler

INPUT_DIR = "./traces/batch_input/"
OUTPUT_DIR = "./traces/results/"

def infer_module_from_filename(filename):
    if filename.startswith("echoos_"):
        return filename.split(".")[0]
    return None

def load_trace_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return [json.loads(line) for line in f.readlines()]

def save_results(module_name, results):
    output_path = os.path.join(OUTPUT_DIR, f"{module_name}_output.jsonl")
    with open(output_path, "w", encoding="utf-8") as f:
        for r in results:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"[INFO] Saved output to {output_path}")

def main():
    scheduler = EchoKernelScheduler()
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    for filename in os.listdir(INPUT_DIR):
        if not filename.endswith(".jsonl"):
            continue
        module = infer_module_from_filename(filename)
        if not module:
            print(f"[WARN] Could not infer module from {filename}")
            continue

        trace_path = os.path.join(INPUT_DIR, filename)
        trace_data = load_trace_file(trace_path)
        print(f"[INFO] Dispatching {filename} → {module} ({len(trace_data)} entries)")

        results = []
        for trace in trace_data:
            result = scheduler.run_module(module, trace)
            results.append(result)

        save_results(module, results)

if __name__ == "__main__":
    main()
