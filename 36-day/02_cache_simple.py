# 02_cache_simple.py
# functools.cache (Python 3.9+)

from functools import cache

@cache
def cube(n):
    print("Computing cube for", n)
    return n**3

print(cube(3))
print(cube(3))  # cached
