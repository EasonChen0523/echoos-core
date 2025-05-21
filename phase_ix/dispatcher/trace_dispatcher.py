
# trace_dispatcher.py
# EchoOS Phase IX – Batch trace reader and module dispatcher

import json
import os
import sys
from scheduler.EchoKernelScheduler import EchoKernelScheduler

def load_trace(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return [json.loads(line) for line in f.readlines()]
    except Exception as e:
        print(f"[ERROR] Failed to load trace: {e}")
        return []

def dispatch_trace(scheduler, module_key, trace_data):
    results = []
    for item in trace_data:
        result = scheduler.run_module(module_key, item)
        results.append(result)
    return results

def save_results(output_path, results):
    try:
        with open(output_path, "w", encoding="utf-8") as f:
            for entry in results:
                f.write(json.dumps(entry, ensure_ascii=False) + "\n")
        print(f"[INFO] Saved results to {output_path}")
    except Exception as e:
        print(f"[ERROR] Failed to save results: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python trace_dispatcher.py <trace_path> <module_key> <output_path>")
        sys.exit(1)

    trace_path = sys.argv[1]
    module_key = sys.argv[2]
    output_path = sys.argv[3]

    scheduler = EchoKernelScheduler()
    trace_data = load_trace(trace_path)
    results = dispatch_trace(scheduler, module_key, trace_data)
    save_results(output_path, results)
