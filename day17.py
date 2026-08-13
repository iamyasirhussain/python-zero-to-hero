# def has_duplicate(items):
#     seen = {}
#     for item in items:
#         if item in seen:
#             print("Seen so far: ", seen)
#             return True
#         seen[item] = True
#     print("Seen so far: ", seen)   
#     return False

# print(has_duplicate(["web1", "web2", "web1"]))
# print(has_duplicate(["web1", "web2", "web3"]))

# Challenge
"""
Write a function first_duplicate(items) that 
returns the first item that appears twice as you scan left to right.
If there are no duplicates, return None.

python
print(first_duplicate(["web1", "web2", "web3", "web2", "web1"]))   # → web2
print(first_duplicate(["a", "b", "c"]))                            # → None
print(first_duplicate([5, 3, 5, 3]))                               # → 5
"""

def first_duplicate(items):
    seen = {}
    for item in items:
        if item in seen:
            return item
        seen[item] = True
    return None
print(first_duplicate(["web1", "web2", "web3", "web2", "web1"]))   # → web2
print(first_duplicate(["a", "b", "c"]))                            # → None
print(first_duplicate([5, 3, 5, 3]))                               # → 5

