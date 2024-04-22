# 04_defaultdict_example.py
# defaultdict automatically creates default values

from collections import defaultdict

d = defaultdict(int)
words = ["hi", "hello", "hi", "welcome"]

for w in words:
    d[w] += 1

print("DefaultDict count:", dict(d))
