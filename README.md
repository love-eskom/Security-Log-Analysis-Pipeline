# 🔐 Python SOC Detection System

## 📌 Overview

This project is a **Security Operations Center (SOC) simulation tool** built in Python. It generates logs, parses them into structured data, and detects suspicious activities such as brute force attacks and malicious command execution.

---

## 🚀 Features

* 🧾 Log generation (simulated system activity)
* 🔍 Log parsing using regex
* ⚙️ Structured data processing (Python dictionaries)
* 🚨 Detection engine:

  * Brute force attack detection
  * After-hours login detection
  * PowerShell execution detection
* 📊 Alert reporting:

  * Console output
  * JSON export
  * CSV export

---

## 🛠 Tech Stack

* Python
* Regex (`re`)
* OOP (Object-Oriented Programming)
* File handling
* JSON / CSV

---

## 📁 Project Structure

```
SOC project/
│
├── logs/
│   ├── sample.log
│   └── alerts.json
│
├── soc/
│   ├── main.py
│   ├── generate_log.py
│   ├── parser.py
│   ├── detector.py
│   └── reporter.py
```

---

## ⚙️ How It Works

1. **Log Generator**

   * Simulates system activity and writes logs to a file

2. **Parser**

   * Reads logs
   * Uses regex to extract:

     * timestamp
     * event type
     * user
     * IP address

3. **Detection Engine**

   * Applies rules to detect suspicious activity:

     * Multiple failed logins (brute force)
     * Logins at unusual hours
     * PowerShell execution

4. **Reporter**

   * Outputs alerts
   * Saves results as JSON/CSV

---

## ▶️ How to Run

```bash
python soc/main.py
```

---

## 📊 Example Output

```
[HIGH] Brute Force → {'ip': '192.168.1.194'}
[HIGH] PowerShell Execution → {'user': 'admin'}
```

---

## 📌 Future Improvements

* Real-time log monitoring
* CLI interface
* MITRE ATT&CK mapping
* Web dashboard visualization

---

## 🧠 What I Learned

* Regex for data extraction
* OOP design for modular systems
* Log analysis and detection logic
* Building real-world security tools

---

## 📎 Author

* Khulekani Thabethe
