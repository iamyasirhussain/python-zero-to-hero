"""
Challenge of the day

You've got a fleet of servers, each stored as a dictionary, all inside a list.
Loop through them and count how many are healthy vs. critical.
"""

fleet = [
    {"name": "web1", "status": "healthy"},
    {"name": "web2", "status": "critical"},
    {"name": "web3", "status": "healthy"},
    {"name": "web4", "status": "critical"},
    {"name": "web5", "status": "healthy"},

]
healthy = 0
critical = 0

for server in fleet:
    if server["status"] == "healthy":
        healthy += 1
    elif server["status"] == "critical":
        critical += 1
print(f"Healthy: {healthy}, Critical: {critical}")


