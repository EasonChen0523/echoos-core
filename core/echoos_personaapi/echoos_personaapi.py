
# echoos_personaapi.py
# EchoOS Phase VI Module – echoos_personaapi
# Persona tag injector and modifier

def run(input):
    pid = input.get("persona", "Generic")
    text = input.get("input_text", "")
    return {
        "persona": pid,
        "modified_input": f"[{pid}] {text}"
    }
