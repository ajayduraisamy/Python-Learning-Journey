# 03_combinations_with_replacement.py
# combinations_with_replacement example

from itertools import combinations_with_replacement

items = [0, 1, 2]
comb_wr = list(combinations_with_replacement(items, 2))
print("Combinations with replacement (2):", comb_wr)
