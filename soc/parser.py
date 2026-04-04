import re
from datetime import datetime

class LogParser:
    def __init__(self, file_path):
        self.file_path = file_path
    
    def parse_log(self):
        logs = []
        
        pattern = r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) user=(\w+) ip=([\d\.]+)"
        
        with open(self.file_path, "r") as file:
            for line in file:
                line = line.strip()
                
                match = re.match(pattern, line)
                
                if match:
                    timestamp_str, event, user, ip = match.groups()
                    
                    log_entry = {
                        "timestamp": datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S"),
                        "event": event,
                        "user": user,
                        "ip": ip
                    }
                    
                    logs.append(log_entry)
                
                else:
                    print(f"[WARNING] Skipping invalid log: {line}")
        
        return logs