#Challenge of the day

#You've got a list of CPU readings from your fleet. Find the highest one and report it.

readings = [45, 88, 95, 20, 72, 91]
biggest = readings[0]

for item in readings:
    if item > biggest:
        biggest = item
print(f"Highest CPU reading: {biggest}")
