import random

def collect_cloud_data():
    print("[*] Collecting data from cloud providers...")
    sample_data = [
        {
            "instance_id": f"i-{random.randint(1000, 9999)}",
            "region": "us-west-2",
            "public_ip": random.choice([True, False]),
            "ssh_open": random.choice([True, False]),
            "tags": {"Environment": "Dev"}
        }
        for _ in range(5)
    ]
    return sample_data
