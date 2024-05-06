# 06_cmp_to_key.py
# Sorting using cmp_to_key custom comparison

from functools import cmp_to_key

data = [5, -1, 3, 0, 10]

# sort negative first, then positive
def custom_cmp(a, b):
    if (a < 0 and b >= 0): return -1
    if (a >= 0 and b < 0): return 1
    return a - b

sorted_list = sorted(data, key=cmp_to_key(custom_cmp))
print("Custom sorted:", sorted_list)
