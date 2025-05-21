
# EchoOS /core/ Modules (Phase VI)

This directory contains the foundational modules of the EchoOS semantic operating system.

---

## 📦 Included Modules

| Module Name             | Description                                                              |
|--------------------------|--------------------------------------------------------------------------|
| `echoos_kernel`          | Core dispatcher and execution router for semantic operations.            |
| `echoos_promptsystem`    | Prompt modifier for system-level structural injection and style tagging. |
| `echoos_moduleconfinement` | Restricts operator calls based on phase or context.                     |
| `echoos_modulerecovery`  | Handles failed operator execution and performs fallback dispatch.        |
| `echoos_executionnode`   | Triggers a specific semantic operation and logs result traces.           |
| `echoos_crisisdetection` | *(Not yet implemented)* Placeholder for semantic anomaly monitoring.     |

---

## 🔁 Structure

Each module includes:

- `OperatorSpec_echoos_<mod>.md` — Description and usage guide  
- `echoos_<mod>.py` — Runtime logic  
- `echoos_<mod>.trace.template.jsonl` — Test input sample  
- `README_echoos_<mod>.md` — Individual module documentation

---

## 🧠 Design Principle

Each `/core/` module serves as a minimal, testable, and composable semantic component.  
Phase VI establishes the operational groundwork for semantic execution across all future phases.
