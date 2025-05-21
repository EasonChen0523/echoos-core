
# echoos_promptsystem.py
# EchoOS Phase VI Module – echoos_promptsystem
# System prompt formatter and semantic enhancer

def run(input):
    text = input.get("text", "")
    mode = input.get("mode", "default")
    prefix = f"[SYSTEM:MODE={mode}]"
    return {
        "transformed": f"{prefix}\n{text}"
    }
