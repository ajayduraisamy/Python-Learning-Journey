# 02_combinations.py
# combinations example

from itertools import combinations

items = ["a", "b", "c", "d"]

# 2-combinations
comb2 = list(combinations(items, 2))
print("Combinations (2):", comb2)

# combinations without replacement default behaviour
print("Combinations total:", len(list(combinations(items, 2))))
