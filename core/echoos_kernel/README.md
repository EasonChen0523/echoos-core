
# EchoOS /core/ Modules

This directory contains the core execution modules of the EchoOS semantic operating system.  
Each module defines a fundamental semantic mechanism within the EchoOS runtime and is registered as part of Phase VI.

---

## 📦 Modules Included

| Module Name         | Description                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| `echoos_kernel`     | Semantic runtime nucleus. Dispatches trace input to appropriate operators. |
| `echoos_promptsystem` | (To be defined) Handles system-level prompt injection and modulation.      |
| `echoos_tracehub`   | (To be defined) Core trace I/O handler and segment archival interface.     |
| `echoos_modchain`   | (To be defined) Manages module chaining logic and flow control.            |
| `echoos_personaapi` | (To be defined) Interface layer for persona access and modulation control. |

---

## 🧠 Purpose

Each module in `/core/` is a lightweight, single-responsibility semantic operator.  
They form the foundational substrate for higher-phase orchestration (e.g., Phase VII/VIII).

---

## 📂 Structure

Each module includes:

- `OperatorSpec_echoos_<name>.md` → Specification and usage format
- `echoos_<name>.py` → Executable Python module logic
- `echoos_<name>.trace.template.jsonl` → Sample input for testing and validation

---

## ✅ Module Readiness

Modules marked as **implemented** contain real logic and support trace input simulation.

