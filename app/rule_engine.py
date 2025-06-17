def evaluate_rules(resource: dict):
    violations = []
    if resource.get("public_ip") and resource.get("ssh_open"):
        violations.append("Public IP with SSH open")
    if resource["tags"].get("Environment") not in ["Prod", "Staging"]:
        violations.append("Improper environment tag")
    return violations
