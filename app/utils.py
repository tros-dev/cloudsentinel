def normalize_resource_name(name):
    return name.lower().replace(" ", "_")

def redact_sensitive_data(data):
    if "secret" in data:
        data["secret"] = "***REDACTED***"
    return data
