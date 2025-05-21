
# echoos_moduleconfinement.py
# EchoOS Phase VI Module – echoos_moduleconfinement
# Semantic operator execution boundary validator

def run(input):
    op = input.get("op", "")
    phase = input.get("phase", "")
    blocklist = {
        "VIII": ["× PROJECT(N)", "× TRACE FLOW"]
    }
    blocked = blocklist.get(phase, [])
    return {
        "allowed": op not in blocked,
        "reason": None if op not in blocked else f"Operator not allowed in phase {phase}"
    }
