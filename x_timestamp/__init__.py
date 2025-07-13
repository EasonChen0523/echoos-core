"""
Shim package: re-export helpers from ×_TIMESTAMP so we can
`import x_timestamp.timestamp_util` everywhere.
"""
import importlib.util as util
from pathlib import Path
import sys

from pathlib import Path
import importlib.util as util
import sys

ROOT = Path(__file__).resolve().parent.parent   # = …/echoos-core
ts_path = ROOT / "phase-x" / "modules" / "×_TIMESTAMP" / "timestamp_util.py"

spec = util.spec_from_file_location("x_timestamp.timestamp_util", ts_path)
module = util.module_from_spec(spec)
spec.loader.exec_module(module)          # type: ignore[attr-defined]

# 將子模組註冊到 sys.modules，之後其它檔僅需常規 import
sys.modules[__name__ + ".timestamp_util"] = module
