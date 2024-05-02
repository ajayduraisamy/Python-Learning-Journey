# 05_multiprocessing_exercises.py
# Practice tasks

from multiprocessing import Pool
import time

# 1. Double numbers
def double(n):
    time.sleep(0.2)
    return n * 2

with Pool(3) as p:
    print("Doubles:", p.map(double, range(1, 11)))

# 2. Calculate cube using processes
def cube(n):
    return n ** 3

with Pool(4) as p:
    print("Cubes:", p.map(cube, [2, 4, 6, 8]))
