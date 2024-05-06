# 01_lru_cache.py
# functools.lru_cache example

from functools import lru_cache
import time

@lru_cache(maxsize=128)
def slow_square(n):
    time.sleep(0.3)
    return n * n

print(slow_square(5))
print("Cached:", slow_square(5))  # instant
