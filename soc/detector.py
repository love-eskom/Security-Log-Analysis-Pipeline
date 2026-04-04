from collections import defaultdict
from datetime import timedelta

class DetectionEngine:
    def __init__(self, logs):
        self.logs = logs
        
    def detect_brute(self):
        alerts = []
        failed_attempts = defaultdict(list)
        
        for log in self.logs:
            if log["event"] == "LOGIN_FAILED":
                failed_attempts[log["ip"]].append(log["timestamp"])
        
        for ip, timestamps in failed_attempts.items():
            timestamps.sort()

            for i in range(len(timestamps) - 2):
                t1 = timestamps[i]
                t2 = timestamps[i + 2]

                if (t2 - t1) <= timedelta(seconds=60):
                    alerts.append({
                        "type": "Brute Force",
                        "ip": ip,
                        "severity": "HIGH"
                    })
                    break   # avoid duplicate alerts
                    
        return alerts
    
    
    def detect_after_hours(self):
        alerts = []
        
        for log in self.logs:
            hour = log["timestamp"].hour

            if log["event"] == "LOGIN_SUCCESS" and (hour < 5):
                alerts.append({
                    "type": "After Hours Login",
                    "user": log["user"],
                    "time": log["timestamp"],
                    "severity": "MEDIUM"
                })
    
        return alerts


    def detect_powershell(self):
        alerts = []
        
        for log in self.logs:
            if log["event"] == "POWERSHELL_EXECUTION":
                alerts.append({
                    "type": "PowerShell Execution",
                    "user": log["user"],
                    "time": log["timestamp"],
                    "severity": "HIGH"
                })
                
        return alerts


    def run_all_detections(self):
        alerts = []
        alerts.extend(self.detect_brute())
        alerts.extend(self.detect_powershell())
        alerts.extend(self.detect_after_hours())
        
        return alerts