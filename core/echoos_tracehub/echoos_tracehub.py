
# echoos_tracehub.py
# EchoOS Phase VI Module – echoos_tracehub
# Handles reading/writing .jsonl trace files

import json

def run(input):
    trace_path = input.get("trace_path")
    output_path = input.get("output_path")

    try:
        with open(trace_path, "r", encoding="utf-8") as f:
            lines = [json.loads(line) for line in f.readlines()]
        with open(output_path, "w", encoding="utf-8") as f:
            for entry in lines:
                f.write(json.dumps(entry, ensure_ascii=False) + "\n")
        return {
            "status": "written",
            "entries": len(lines)
        }
    except Exception as e:
        return {
            "status": "error",
            "error": str(e)
        }
