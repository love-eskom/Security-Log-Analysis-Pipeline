import os
from datetime import datetime

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def write_log(file, timestamp, event, user, ip):
    log_line = f"{timestamp} {event} user={user} ip={ip}"
    file.write(log_line + "\n")


def generate_logs():
    base_dir = os.path.dirname(os.path.dirname(__file__))
    log_path = os.path.join(base_dir, "logs", "sample.log")

    with open(log_path, "w") as file:    
        #normal activity
        write_log(file, "2026-03-30 16:26:33", "LOGIN_SUCCESS", "Zanele", "192.168.1.16")
        write_log(file, "2026-03-30 16:26:33", "LOGIN_SUCCESS", "Michael", "192.168.1.19")
        
        # brute force        
        basetime = "2026-03-01 09:05:3"
        for i in range(5):
            timestamp = f"{basetime}{i}"
            write_log(file, timestamp, "LOGIN_FAILED", "admin", "192.168.1.194")
            
        #suspicious activity
        write_log(file, "2026-03-01 23:50:10", "POWERSHELL_EXECUTION", "admin", "192.168.1.2")
    