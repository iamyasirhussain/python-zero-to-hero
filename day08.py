def greet(name):
    print(f"Deploying app to {name}...")


greet("web1")
greet("web2")

def add_replicas(current, extra):
    return current + extra

result = add_replicas(3, 2)
print(f"New replica count: {result}")

"""
Challenge of the day

Write a function called health_check that takes a CPU percentage and
returns the right status string (doesn't print it — returns it):

90 or above → returns "CRITICAL"
70 or above (under 90) → returns "WARNING"
else → returns "OK"
"""
def health_check(cpu):
    if cpu >= 90:
        return "CRITICAL"
    if cpu >= 70:
        return "WARNING"
    return "OK"

#result = health_check(int(input("What is the CPU usage? ")))
print(health_check(95))
print(health_check(75))
print(health_check(30))
