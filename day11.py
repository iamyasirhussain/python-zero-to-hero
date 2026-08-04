# try:
#     age = int(input("Age: "))
#     print(f"Next year you'll be {age + 1}")
# except ValueError:
#     print("That's not a valid number!")
"""
Challenge of the day

Write a function safe_divide(a, b) that divides a by b and returns 
the result — but handles the classic crash: dividing by zero.

Normal case: safe_divide(10, 2) → returns 5.0
Danger case: safe_divide(10, 0) → instead of crashing, returns the string "Cannot divide by zero"

Test it:

python
print(safe_divide(10, 2))    # → 5.0
print(safe_divide(10, 0))    # → Cannot divide by zero
print(safe_divide(20, 4))    # → 5.0
"""

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"

print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_divide(20, 4))
