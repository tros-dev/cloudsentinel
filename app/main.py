from fastapi import FastAPI
from app.collector import collect_cloud_data
from app.rule_engine import evaluate_rules
from app.alerting import send_alert
from app.dashboard import get_dashboard_data

app = FastAPI(title="CloudSentinel")

@app.get("/audit")
def run_audit():
    data = collect_cloud_data()
    alerts = []
    for item in data:
        violated_rules = evaluate_rules(item)
        if violated_rules:
            alert = send_alert(item, violated_rules)
            alerts.append(alert)
    return {"alerts": alerts}

@app.get("/dashboard")
def dashboard():
    return get_dashboard_data()
