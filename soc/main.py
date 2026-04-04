from parser import LogParser
from detector import DetectionEngine 
from reporter import ReportGenerator

log_parser = LogParser("logs/sample.log")
logs = log_parser.parse_log()

detector = DetectionEngine(logs)
alerts = detector.run_all_detections()


reporter = ReportGenerator(alerts)
reporter.save_to_json("logs/logs.json")
reporter.save_to_csv("logs/logs.csv")

for alert in alerts:
    print(f"[{alert['severity']}] {alert['type']} → {alert}\n")