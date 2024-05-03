# 14_partial_functions.py
# Using functools.partial

from functools import partial

def power(a, b):
    return a ** b

square = partial(power, b=2)
cube = partial(power, b=3)

print("Square 7:", square(7))
print("Cube 5:", cube(5))
