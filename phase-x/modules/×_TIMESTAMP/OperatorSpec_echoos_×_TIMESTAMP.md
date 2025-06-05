# Operator Specification: × TIMESTAMP

## Phase
- Phase VI (core metadata operator)
- Phase IX (automated trace integration)

## Function
Inserts or updates the `timestamp` field in a semantic trace using the ISO 8601 UTC format.

## Format
```json
{
  "metadata": {
    "timestamp": "2025-06-05T14:00:00Z"
  }
}
