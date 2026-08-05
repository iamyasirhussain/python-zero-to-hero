import json

config = {
    "app_name": "payments-api",
    "replicas": 3,
    "env": "production",
    "features": ["logging", "metrics", "tracing"]
}

with open("config.txt", "w") as f:
    json.dump(config, f)


with open("config.txt", "r") as f:
    data = json.load(f)
 
print(f"App: {data['app_name']}")
print(f"Replicas: {data['replicas']}")
print(f"Features: {len(data['features'])} enabled")
