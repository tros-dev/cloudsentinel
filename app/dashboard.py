from datetime import datetime

def get_dashboard_data():
    return {
        "status": "ok",
        "timestamp": datetime.utcnow().isoformat(),
        "message": "Welcome to CloudSentinel",
        "sample_metrics": {
            "audited_instances": 5,
            "critical_findings": 2,
            "regions_covered": 1
        }
    }
