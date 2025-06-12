
# EchoKernelScheduler.py
# EchoOS Phase IX – Semantic Module Dispatcher and Runtime Controller

import importlib
import json
import os
from pathlib import Path

MODULE_PATHS = {
    "echoos_kernel": "core/echoos_kernel/echoos_kernel.py",
    "echoos_promptsystem": "core/echoos_promptsystem/echoos_promptsystem.py",
    "echoos_moduleconfinement": "core/echoos_moduleconfinement/echoos_moduleconfinement.py",
    "echoos_modulerecovery": "core/echoos_modulerecovery/echoos_modulerecovery.py",
    "echoos_executionnode": "core/echoos_executionnode/echoos_executionnode.py",
    "echoos_crisisdetection": "core/echoos_crisisdetection/echoos_crisisdetection.py",
    # Phase VIII
    "filter_noise": "phase-viii/filter/x_filter_noise.py",
    "suppress_noise": "phase-viii/suppress/x_suppress_noise.py",
    "histo_balance": "phase-viii/histo/x_histo_balance.py",
    "enhance_contrast": "phase-viii/enhance/x_enhance_contrast.py",
    "dehaze_tone": "phase-viii/dehaze/x_dehaze_tone.py",
    # Phase VII
    "x_edge": "phase-vii/edge/x_edge.py",
    "x_fuse": "phase-vii/fuse_mesh/x_fuse.py",
    "x_segment": "phase-vii/segment/x_segment.py",
    "x_smooth": "phase-vii/smooth/x_smooth.py",
    "x_trace_flow": "phase-vii/trace_flow/x_trace_flow.py",
    "x_projectn": "phase-vii/project_n/x_projectn.py",
    "x_shrink": "phase-vii/shrink/x_shrink.py",
    "x_expand": "phase-vii/expand/x_expand.py",
    "x_reseal": "phase-vii/reseal/x_reseal.py",
    "x_highlight": "phase-vii/highlight/x_highlight.py",
}

BASE_DIR = Path(__file__).resolve().parents[2]

def dynamic_import(path):
    import importlib.util
    abs_path = (BASE_DIR / path).resolve()
    module_name = abs_path.stem
    spec = importlib.util.spec_from_file_location(module_name, abs_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

class EchoKernelScheduler:
    def __init__(self):
        self.loaded_modules = {}

    def run_module(self, module_key, input_data):
        if module_key not in MODULE_PATHS:
            return {"status": "error", "error": f"Unknown module: {module_key}"}
        try:
            if module_key not in self.loaded_modules:
                self.loaded_modules[module_key] = dynamic_import(MODULE_PATHS[module_key])
            module = self.loaded_modules[module_key]
            return module.run(input_data)
        except Exception as e:
            return {"status": "error", "error": str(e)}

# Example usage
if __name__ == "__main__":
    scheduler = EchoKernelScheduler()
    result = scheduler.run_module("echoos_promptsystem", {
        "text": "summarize the trace",
        "mode": "brief"
    })
    print(json.dumps(result, indent=2))
