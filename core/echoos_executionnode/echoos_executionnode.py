
# echoos_executionnode.py
# EchoOS Phase VI Module – echoos_executionnode
# Node for dispatching a semantic operator invocation

def run(input):
    op = input.get("operator")
    trace = input.get("trace", [])
    filtered = []
    for seg in trace:
        text = seg.get("text", "")
        clean = " ".join([w for w in text.split() if w.lower() not in {"uh", "well", "i", "guess"}])
        filtered.append({"id": seg.get("id"), "filtered": clean})
    return {
        "status": "success",
        "output_trace": filtered
    }
