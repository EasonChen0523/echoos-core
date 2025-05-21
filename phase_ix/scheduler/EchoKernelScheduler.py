
# EchoKernelScheduler.py
# EchoOS Phase IX – Semantic Module Dispatcher and Runtime Controller

import importlib
import json
import os

MODULE_PATHS = {
    "echoos_kernel": "/core/echoos_kernel.py",
    "echoos_promptsystem": "/core/echoos_promptsystem.py",
    "echoos_moduleconfinement": "/core/echoos_moduleconfinement.py",
    "echoos_modulerecovery": "/core/echoos_modulerecovery.py",
    "echoos_executionnode": "/core/echoos_executionnode.py",
    "echoos_crisisdetection": "/core/echoos_crisisdetection.py",
    # Phase VIII
    "filter_noise": "/phase-viii/filter/x_filter_noise.py",
    "suppress_noise": "/phase-viii/suppress/x_suppress_noise.py",
    "histo_balance": "/phase-viii/histo/x_histo_balance.py",
    "enhance_contrast": "/phase-viii/enhance/x_enhance_contrast.py",
    "dehaze_tone": "/phase-viii/dehaze/x_dehaze_tone.py",
    # Phase VII
    "x_edge": "/phase-vii/x_edge.py",
    "x_fuse": "/phase-vii/x_fuse.py",
    "x_segment": "/phase-vii/x_segment.py",
    "x_smooth": "/phase-vii/x_smooth.py",
    "x_trace_flow": "/phase-vii/x_trace_flow.py",
    "x_projectn": "/phase-vii/x_projectn.py"
}

def dynamic_import(path):
    import importlib.util
    module_name = os.path.splitext(os.path.basename(path))[0]
    spec = importlib.util.spec_from_file_location(module_name, path)
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
