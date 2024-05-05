# 10_recipes_examples.py
# Small real-world recipes using itertools helpers

from itertools import combinations, product
from operator import add

# pairs for comparison
items = ['cpu','gpu','ram','ssd']
pairs = list(combinations(items, 2))
print("Pairs:", pairs)

# build configuration combinations
sizes = ['small','medium']
colors = ['black','white']
configs = list(product(sizes, colors))
print("Configs:", configs)
