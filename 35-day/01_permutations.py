# 01_permutations.py
# permutations example

from itertools import permutations

items = [1, 2, 3]
perms = list(permutations(items, 2))  # length-2 permutations
print("Permutations (length 2):", perms)

# all full-length permutations
print("All permutations:", list(permutations(items)))
