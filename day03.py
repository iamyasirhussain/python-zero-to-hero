name = input("what is your name? ")
age = int(input("How old are you? "))
print(f"Hey {name}, welcome aboard!")
print(f"Next year you'll be {age + 1}")


# Challeng day 3

pods = int(input("How many pods are running? "))
each_pod_memory = int(input("How much memory does each pod use? "))
total_memory = pods * each_pod_memory

print(f"{pods} pods x {each_pod_memory} MB = {total_memory} MB total")