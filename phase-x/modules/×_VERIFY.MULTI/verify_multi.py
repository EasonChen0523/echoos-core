# verify_multi.py

import json
from datetime import datetime

def verify_multi(trace):
    outputs = trace.get("model_outputs", {})
    keys = list(outputs.keys())

    if len(keys) < 2:
        return {"error": "At least two models required for verification."}

    base_output = outputs[keys[0]]
    divergence = {
        "score": 0.0,
        "key_semantic_shift": [],
        "conflict_zones": []
    }

    for key in keys[1:]:
        if outputs[key] != base_output:
            divergence["score"] += 1
            divergence["conflict_zones"].append(key)

    divergence["score"] /= (len(keys) - 1)

    return {
        "trace_id": trace.get("trace_id"),
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "drift_report": divergence,
        "verdict": "Agreement" if divergence["score"] == 0 else "Partial or Full Divergence"
    }
