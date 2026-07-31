servers = ["web1", "web2", "web3"]
for server in servers:
    print(f"Checking {server}")

for i in range(3):
    print(f"Attempt number {i}")
# Challenge: 
"""
Build a fleet health monitor. You've got a list of servers, 
each with a CPU reading. Loop through them and print a status
for each one using yesterday's thresholds.
"""

readings = [("web1", 45), ("web2", 88), ("web3", 95), ("web4", 20)]

for name, cpu in readings:
    if cpu >= 90:
        print(f"{name}: CRITICAL ({cpu}%)")
    elif cpu >= 70:
        print(f"{name}: WARNING ({cpu}%)")
    else:
        print(f"{name}: OK ({cpu}%)")
