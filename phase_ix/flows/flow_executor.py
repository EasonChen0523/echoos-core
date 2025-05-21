
# flow_executor.py
# EchoOS Phase IX – Execute modular semantic flow chains

import json
import os
import sys
from scheduler.EchoKernelScheduler import EchoKernelScheduler

def execute_flow(flow_path):
    try:
        with open(flow_path, "r", encoding="utf-8") as f:
            flow = json.load(f)
    except Exception as e:
        print(f"[ERROR] Failed to load flow: {e}")
        return

    print(f"[INFO] Executing flow: {flow.get('flow_name')}")
    scheduler = EchoKernelScheduler()
    results = []
    for i, step in enumerate(flow.get("steps", [])):
        module = step.get("module")
        input_data = step.get("input")
        print(f"[STEP {i+1}] → {module}")
        output = scheduler.run_module(module, input_data)
        results.append({
            "step": i + 1,
            "module": module,
            "input": input_data,
            "output": output
        })
    return results

def save_results(results, output_path):
    try:
        with open(output_path, "w", encoding="utf-8") as f:
            for entry in results:
                f.write(json.dumps(entry, ensure_ascii=False) + "\n")
        print(f"[INFO] Results saved to {output_path}")
    except Exception as e:
        print(f"[ERROR] Failed to save output: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python flow_executor.py <flow_path> <output_path>")
        sys.exit(1)

    flow_path = sys.argv[1]
    output_path = sys.argv[2]

    result_data = execute_flow(flow_path)
    if result_data:
        save_results(result_data, output_path)
