def is_palindrom(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left = left + 1
        right = right - 1
    return True

print(is_palindrom("racecar"))
print(is_palindrom("hello"))

"""
Challenge of the day

Write reverse_string(s) that reverses a list of characters in place using two pointers — 
swapping from both ends toward the middle.

python
chars = ["h", "e", "l", "l", "o"]
reverse_string(chars)
print(chars)     # → ['o', 'l', 'l', 'e', 'h']

The rule: do it with two pointers and O(1) space — no creating a new list, no chars[::-1] 
shortcut, no .reverse(). Swap elements within the same list. 
That's what "in place" means — you modify the original, using no extra memory.
"""
def reverse_string(s):
    left = 0
    right = len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left = left + 1
        right = right - 1

chars = ["h", "e", "l", "l", "o"]
reverse_string(chars)
print(chars)
