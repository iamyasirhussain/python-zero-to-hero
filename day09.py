def total(numbers):
    result = 0
    for n in numbers:
        result = result + n
    return result

print(total([10, 20, 30]))

"""
Challenge of the day — your first LeetCode-flavored problem

Write a function count_evens(numbers) that takes a list of numbers and 
returns how many of them are even.

python
print(count_evens([1, 2, 3, 4, 5, 6]))   # → 3   (2, 4, 6 are even)
print(count_evens([1, 3, 5]))            # → 0
print(count_evens([2, 4, 8, 10]))        # → 4
"""
def count_evens(numbers):
    even_counter = 0
    for number in numbers:
        if number % 2 == 0:
            even_counter += 1
    return even_counter
print(count_evens([1, 2, 3, 4, 5, 6]))
print(count_evens([1, 3, 5]))
print(count_evens([2, 4, 8, 10]))
