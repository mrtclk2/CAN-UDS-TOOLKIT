# CAN-UDS Toolkit

This repository is my learning project about **CAN Bus** and **UDS**.  
The goal is to keep notes, small examples and simple scripts while I practice automotive diagnostics.

---

## Contents
- **docs/** → short notes about CAN and UDS  
- **examples/** → sample CAN log files  
- **src/** → small Python scripts (log parser etc.)  

---

## How to try
There is a very simple script in `src/uds-log-parser.py`.  
It reads the sample log in `examples/can_log_sample.asc` and prints some UDS messages.

Run with:
```bash
python src/uds-log-parser.py
