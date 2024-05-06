# 03_partial_advanced.py
# functools.partial advanced usage

from functools import partial

def power(base, exp):
    return base ** exp

square = partial(power, exp=2)
cube = partial(power, exp=3)

print("Square 7:", square(7))
print("Cube 3:", cube(3))
