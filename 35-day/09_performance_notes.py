# 09_performance_notes.py
# Notes: lazy iterators vs lists; memory & performance

from itertools import islice

# Example: avoid creating huge lists when unnecessary
big = range(10**6)

# take first 5 lazily
first5 = list(islice(big, 5))
print("First 5 from big range:", first5)

# Use generator expressions or itertools to keep memory low
gen = (x*x for x in range(1000000))
print("Generator created, not evaluated")
print("Next element:", next(gen))
