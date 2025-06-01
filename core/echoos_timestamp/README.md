# EchoOS Operator: × TIMESTAMP

This module provides system time injection functionality into semantic trace records.

- Phase: VI (core operator) + IX (execution support)
- Output: Appends a timestamp field (ISO 8601, default UTC+8) to each trace entry
- Applications:
  - Time-based drift tracking for SGNN nodes
  - Trace temporal indexing
  - Causality-aware reasoning across modules
