<div align="center">

# Security Log Analysis Pipeline

A Python-based security monitoring simulation for synthetic log generation, regex event parsing, rule-based detection, and structured alert reporting.

`PYTHON` · `LOG ANALYSIS` · `DETECTION`

</div>

---

## Overview

The Security Log Analysis Pipeline simulates an end-to-end Security Operations Center (SOC) log monitoring workflow. It generates synthetic system activity logs, parses raw entries into structured event dictionaries using regular expressions, evaluates events against behavioural detection rules, and outputs machine-readable alerts in JSON and CSV formats.

## Capabilities

- **Synthetic Log Generation:** Generates simulated system activity entries and writes raw events to `logs/sample.log`.
- **Regex Event Parsing:** Extracts timestamps, event types, usernames, and source IP addresses from raw log lines into structured Python dictionaries.
- **Brute-Force Detection:** Flags repeated failed login attempts originating from the same IP address.
- **After-Hours Login Detection:** Identifies authentication events occurring outside standard operating hours.
- **PowerShell Execution Detection:** Flags PowerShell process execution events within the parsed log stream.
- **Multi-Format Alert Reporting:** Prints alerts to the console and exports findings to JSON (`logs/alerts.json`) and CSV formats.

## Architecture

The pipeline processes log data sequentially across four decoupled modules coordinated by `main.py`:

``` text 
Synthetic Log Generation (generate_log.py)
        │
        ▼
  Raw Log File (logs/sample.log)
        │
        ▼
Regex Event Parsing (parser.py)
        │
        ▼
Structured Event Dictionaries
        │
        ▼
Rule-Based Detection Engine (detector.py)
        │
        ▼
Alert Reporting & Export (reporter.py)
   ├──► Console Output
   ├──► JSON (logs/alerts.json)
   └──► CSV Export
```

## Project Structure
``` text 
Security-Log-Analysis-Pipeline/

├── logs/
│   ├── sample.log
│   └── alerts.json
├── soc/
│   ├── main.py
│   ├── generate_log.py
│   ├── parser.py
│   ├── detector.py
│   └── reporter.py
├── Requirements.txt
└── README.md
```
## Installation 

- git clone [https://github.com/love-eskom/Security-Log-Analysis-Pipeline.git](https://github.com/love-eskom/Security-Log-Analysis-Pipeline.git)

- cd Security-Log-Analysis-Pipeline

## Expected Behaviour:
The script generates simulated log entries in logs/sample.log, parses the events, evaluates detection rules, prints any triggered alerts to the terminal, and saves exported alert files under logs/.

Example console output:

``` Plaintext
[HIGH] Brute Force -> {'ip': '192.168.1.194'}
[HIGH] PowerShell Execution -> {'user': 'admin'}
```
## Testing
Automated unit tests are not yet implemented for this repository. Validation is currently performed by executing python soc/main.py end-to-end and verifying that:

- logs/sample.log populates with formatted log lines.
- Console output reflects expected rule triggers.
- logs/alerts.json and CSV outputs contain valid, structured alert records.

## Limitations
- Synthetic Data Only: Operates on generated sample logs rather than live OS or SIEM event streams.
- Static Rule Thresholds: Detection logic relies on hardcoded rules and time windows rather than external configuration files.
- Batch Processing: Executes as a one-off batch script rather than a continuous real-time log tailer.
- Context-Free PowerShell Alerts: Flags PowerShell execution events without inspecting command-line arguments or script block intent.

## Author
Gcinikhaya Thabethe

[GitHub](https://github.com/love-eskom/)
[LinkedIn](inkedin.com/in/gcinikhaya-thabethe-33167b274/)
