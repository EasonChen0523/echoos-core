"""
EchoOS Operator: × TIMESTAMP
Phase VI + Phase IX Integrated
Purpose: Adds UTC timestamp to semantic trace metadata
"""

from datetime import datetime

def apply_timestamp(trace):
    """
    Adds or replaces the 'timestamp' field in the metadata of the trace.
    Format: ISO 8601 UTC Zulu time
    """
    if "metadata" not in trace:
        trace["metadata"] = {}

    trace["metadata"]["timestamp"] = datetime.utcnow().isoformat() + "Z"
    return trace
