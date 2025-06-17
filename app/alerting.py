import datetime

def send_alert(resource: dict, violations: list):
    alert = {
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "resource": resource["instance_id"],
        "violations": violations
    }
    print(f"[!] Alert: {alert}")
    return alert
