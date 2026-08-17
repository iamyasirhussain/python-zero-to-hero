#Challenge - Two sum
def two_sum(nums, target):
    seen = {}
    for index, number in enumerate(nums):
        compliment = target - number
        if compliment in seen:
            return [seen[compliment], index]
        seen[number]= index
    return None

print(two_sum([2, 7, 11, 15], 9))     # → [0, 1]
print(two_sum([3, 5, 8], 11))         # → [0, 2]
print(two_sum([1, 2, 3], 100))        # → None
