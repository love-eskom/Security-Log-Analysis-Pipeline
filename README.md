
<div align="center">

# Security Log Analysis Pipeline
LAB-003

A Python-based security monitoring simulation for
log generation, event analysis, threat detection
and automated alert reporting.

`PYTHON` · `LOG ANALYSIS` · `DETECTION`

</div>

---

## Overview

The Security Log Analysis Pipeline is a Python-based
security monitoring project designed to simulate
the processing of system activity logs and identify
potentially suspicious behaviour.

The system generates synthetic log data, extracts
structured events using regular expressions, applies
detection rules and produces machine-readable alerts.

It demonstrates a basic security monitoring workflow
through modular Python components.

## Capabilities

- **Log Generation:** Simulates system activity and
  produces sample log files.
- **Event Parsing:** Extracts timestamps, event types,
  usernames and IP addresses using regular expressions.
- **Brute-Force Detection:** Identifies repeated
  failed login attempts.
- **After-Hours Detection:** Identifies login activity
  occurring outside defined hours.
- **PowerShell Detection:** Identifies PowerShell
  execution events in the generated logs.
- **Alert Reporting:** Displays detection results
  and exports alerts to JSON and CSV.

## Architecture

The application follows a sequential processing
workflow.

```text
Synthetic Log Generation
          |
          v
     Log Parsing
          |
          v
  Structured Event Data
          |
          v
   Detection Engine
          |
          v
     Alert Reporting
       /       \
      v         v
    JSON       CSV
```

### Components

| Component | Responsibility |
|---|---|
| Log Generator | Produces synthetic system activity |
| Parser | Extracts structured event information |
| Detector | Evaluates events against detection rules |
| Reporter | Displays and exports generated alerts |
| Main | Coordinates the processing workflow |

## Detection Logic

The detection engine implements three detection
categories:

**Brute-Force Activity**

Identifies repeated failed authentication attempts
associated with an IP address.

**After-Hours Logins**

Identifies authentication activity occurring outside
the configured monitoring hours.

**PowerShell Execution**

Identifies PowerShell execution events within
the simulated log data.

These rules demonstrate basic detection logic and
do not independently establish malicious intent.

## Technology

| Category | Technology |
|---|---|
| Language | Python |
| Parsing | Regular Expressions (`re`) |
| Programming | Object-Oriented Programming |
| Data Processing | Python Dictionaries |
| Reporting | JSON, CSV |
| File Handling | Python Standard Library |

## Project Structure

```text
project/
├── logs/
│   ├── sample.log
│   └── alerts.json
│
└── soc/
    ├── main.py
    ├── generate_log.py
    ├── parser.py
    ├── detector.py
    └── reporter.py
```

## Getting Started

### Prerequisites

- Python 3
- Git

### Installation

Clone the repository:

```bash
git clone https://github.com/love-eskom/Security-Log-Analysis-Pipeline
```

Navigate to the project directory:

```bash
cd security-log-analysis-pipeline
```

### Execution

Run the application from the repository root:

```bash
python soc/main.py
```

The application generates simulated activity,
processes the resulting logs and produces detection
alerts.

## Example Output

```text
[HIGH] Brute Force -> {'ip': '192.168.1.194'}

[HIGH] PowerShell Execution -> {'user': 'admin'}
```

Output shown is illustrative. Actual output depends
on the generated log data and detection configuration.

## Limitations

- Uses synthetic rather than live system logs.
- Detection relies on predefined rules.
- Does not provide real-time monitoring.
- Does not implement a centralised event storage system.
- Detection results depend on the quality and structure
  of the input data.

## Roadmap

- [ ] Implement configurable detection thresholds.
- [ ] Introduce structured event models.
- [ ] Add automated unit testing.
- [ ] Implement real-time log monitoring.
- [ ] Explore MITRE ATT&CK technique mapping.

## Author

**Gcinikhaya Thabethe**

[GitHub](https://github.com/love-eskom) ·
[LinkedIn](https://www.linkedin.com/in/gcinikhaya-thabethe-33167b274)
