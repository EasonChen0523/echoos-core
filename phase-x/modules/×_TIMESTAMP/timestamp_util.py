"""EchoOS Phase‑X – ×_TIMESTAMP
------------------------------------------------
Centralised helpers for **timezone‑aware** timestamp handling.
All public helpers return / accept `datetime.datetime` objects in
Asia/Taipei (UTC+8).

Usage
-----
>>> from phase_x.modules.×_TIMESTAMP.timestamp_util import now, from_trace, iso
>>> ts = from_trace("1720722345123")       # ms‑epoch in trace file
>>> print(iso(ts))
'2025-07-12T18:32:25.123+08:00'

The module is intentionally dependency‑free (uses stdlib `zoneinfo`).
"""
from __future__ import annotations

import re
from datetime import datetime, timezone
from zoneinfo import ZoneInfo
from typing import Any, Union

# ──────────────────────────────────────────────────────────────────────────────
# Constants

_TZ = ZoneInfo("Asia/Taipei")  # single source of truth

# common ISO‑8601 formats present in EchoOS traces
_ISO_PATTERNS = (
    "%Y-%m-%dT%H:%M:%S.%fZ",     # 2025-07-13T09:31:44.123Z ⇒ UTC
    "%Y-%m-%dT%H:%M:%S.%f%z",    # 2025-07-13T17:31:44.123+08:00 ⇒ any tz
    "%Y-%m-%dT%H:%M:%SZ",        # second‑precision
    "%Y-%m-%dT%H:%M:%S%z",
)

_EPOCH_MS_RE = re.compile(r"^[0-9]{13}$")  # 13‑digit milliseconds epoch
_EPOCH_S_RE  = re.compile(r"^[0-9]{10}$")  # 10‑digit seconds epoch

# ──────────────────────────────────────────────────────────────────────────────
# Public helpers

def now() -> datetime:
    """Current time in Asia/Taipei with millisecond precision."""
    return datetime.now(tz=_TZ).replace(microsecond=(datetime.now(tz=_TZ).microsecond // 1000) * 1000)

def iso(ts: datetime | None = None) -> str:
    """Return ISO‑8601 string with timezone offset (+08:00)."""
    if ts is None:
        ts = now()
    return ts.astimezone(_TZ).isoformat(timespec="milliseconds")

def from_trace(raw: Union[str, int, float]) -> datetime:
    """Parse a timestamp value coming from EchoOS trace JSONL.

    Accepts:
    * **ms‑epoch** (13‑digit) – e.g. "1720722345123"
    * **s‑epoch**  (10‑digit) – e.g. "1720722345"
    * **ISO‑8601** strings in the patterns defined above
    * numeric epoch values (int/float)

    Returns `datetime` aware (Asia/Taipei).
    Raises `ValueError` on unrecognised format.
    """
    if isinstance(raw, (int, float)):
        sec = float(raw) / (1000 if raw > 1e12 else 1)
        return datetime.fromtimestamp(sec, tz=_TZ)

    if not isinstance(raw, str):
        raise TypeError("timestamp must be str | int | float")

    raw = raw.strip()

    # 1) epoch milliseconds / seconds as str
    if _EPOCH_MS_RE.match(raw) or _EPOCH_S_RE.match(raw):
        sec = float(raw) / (1000 if len(raw) == 13 else 1)
        return datetime.fromtimestamp(sec, tz=_TZ)

    # 2) ISO‑8601
    for pat in _ISO_PATTERNS:
        try:
            dt = datetime.strptime(raw, pat)
            # attach zone if missing (case "Z" UTC)
            if dt.tzinfo is None or dt.tzinfo == timezone.utc:
                dt = dt.replace(tzinfo=timezone.utc)
            return dt.astimezone(_TZ)
        except ValueError:
            continue

    raise ValueError(f"Unrecognised timestamp format: {raw!r}")

# ──────────────────────────────────────────────────────────────────────────────
# CLI test (optional)

if __name__ == "__main__":
    import json, sys

    for token in sys.argv[1:]:
        try:
            dt = from_trace(token)
            print(f"{token:>30}  →  {iso(dt)}")
        except Exception as e:
            print(f"ERROR for {token}: {e}")
