from datetime import datetime, timezone, timedelta
import json
from pathlib import Path

def inject_timestamp(entry: dict, tz_offset_hours: int = 8) -> dict:
    tz = timezone(timedelta(hours=tz_offset_hours))
    now_iso = datetime.now(tz).isoformat()
    entry["timestamp"] = now_iso
    return entry

def load_trace_file(trace_path: str):
    with open(trace_path, "r", encoding="utf-8") as f:
        return [json.loads(line.strip()) for line in f if line.strip()]

def save_trace_file(traces: list, output_path: str):
    with open(output_path, "w", encoding="utf-8") as f:
        for trace in traces:
            f.write(json.dumps(trace, ensure_ascii=False) + "\n")

def build_trace_with_timestamp(input_path: str, output_path: str):
    traces = load_trace_file(input_path)
    stamped = [inject_timestamp(entry) for entry in traces]
    save_trace_file(stamped, output_path)
    print(f"[Trace Builder] Timestamp injection completed for {len(stamped)} entries.")
