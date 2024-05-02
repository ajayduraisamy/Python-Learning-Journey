# 04_pool_example.py
# Using Pool for parallel execution

from multiprocessing import Pool

def square(n):
    return n * n

with Pool(4) as p:
    results = p.map(square, [1, 2, 3, 4, 5])

print("Squares:", results)
