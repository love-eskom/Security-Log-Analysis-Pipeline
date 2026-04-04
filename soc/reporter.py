import json
import csv
        
class ReportGenerator:
    def __init__(self, alerts):
        self.alerts = alerts

    def save_to_json(self, filepath):
        with open(filepath, "w") as file:
            json.dump(self.alerts, file, default=str, indent=4)

    def save_to_csv(self, filepath):
        # Define all possible fields
        fieldnames = ["type", "ip", "user", "time", "severity"]

        with open(filepath, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

            for alert in self.alerts:
                # Fill missing keys with None
                row = {key: alert.get(key, None) for key in fieldnames}
                writer.writerow(row)