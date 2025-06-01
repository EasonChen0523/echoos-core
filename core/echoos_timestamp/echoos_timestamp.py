from datetime import datetime, timezone, timedelta

def inject_timestamp(entry: dict, tz_offset_hours: int = 8) -> dict:
    tz = timezone(timedelta(hours=tz_offset_hours))
    now_iso = datetime.now(tz).isoformat()
    entry["timestamp"] = now_iso
    return entry
