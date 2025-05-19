
# x_trace_flow.py
# EchoOS Phase VII Module: × TRACE FLOW
# Tracks emotional tension propagation between adjacent segments

def trace_tension_flows(segments):
    results = []
    for i in range(len(segments) - 1):
        current = segments[i]
        next_seg = segments[i + 1]
        delta = round(next_seg["tone_vector"][0] - current["tone_vector"][-1], 3)
        results.append({
            "from": current["id"],
            "to": next_seg["id"],
            "tension_shift": abs(delta),
            "flow_vector": [delta],
            "direction": "rising" if delta > 0 else "falling" if delta < 0 else "stable"
        })
    return results
