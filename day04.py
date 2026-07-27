# memory_usage = 50
# if memory_usage > 80:
#     print("Warning: high memory!")
# elif memory_usage >= 50:
#     print("watch: memory climbing")
# else:
#     print("All good")


"""
Build a CPU health checker. Your script should:

Ask the user for the current CPU usage percentage (a number).
Print a status based on these rules:
90 or above → CRITICAL: CPU at X%
70 or above (but under 90) → WARNING: CPU at X%
anything else → OK: CPU at X%

(The X is whatever they entered.)

Test it with 95, then 70, then 30 — make sure each hits the right branch.
"""
current_usage = int(input("What is the current cpu usage? "))

if current_usage >= 90:
    print(f"CRITICAL: CPU at {current_usage}%")
elif current_usage >= 70:
    print(f"WARNING: CPU at {current_usage}%")
else:
    print(f"OK: CPU at {current_usage}%")
