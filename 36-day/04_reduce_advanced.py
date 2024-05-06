# 04_reduce_advanced.py
# functools.reduce advanced

from functools import reduce

nums = [2, 3, 4, 5]

product = reduce(lambda a, b: a * b, nums)
print("Product:", product)

max_val = reduce(lambda a, b: a if a > b else b, nums)
print("Max value:", max_val)
