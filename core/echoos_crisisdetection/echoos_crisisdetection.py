
# echoos_crisisdetection.py
# EchoOS Phase VI Module – echoos_crisisdetection
# Detects semantic anomaly zones in trace input

def run(input):
    crisis_ids = []
    trace = input.get("trace", [])
    for seg in trace:
        vec = seg.get("tone_vector", [])
        if any(abs(v - vec[i-1]) > 0.6 for i, v in enumerate(vec[1:], 1)):
            crisis_ids.append(seg.get("id"))
    return {
        "status": "crisis_detected" if crisis_ids else "normal",
        "crisis_ids": crisis_ids
    }
