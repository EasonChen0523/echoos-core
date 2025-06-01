# OperatorSpec: × TIMESTAMP

## Phase
VI (definition) + IX (execution trace integration)

## Purpose
Appends system timestamp to semantic trace entries, enabling EchoOS to track the creation time of each segment or module action.

## Output Format
```json
{
  "input": "What did I do yesterday?",
  "output": "You completed three tasks yesterday.",
  "timestamp": "2025-06-01T20:45:00+08:00"
}
```

## Technical Notes
- Injected via `inject_timestamp()` defined in `echoos_timestamp.py`
- Default timezone offset: UTC+8 (can be adjusted)
- Used internally in Phase IX trace builders and SGNN memory chain initializers
