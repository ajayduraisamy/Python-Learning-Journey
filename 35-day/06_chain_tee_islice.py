# 06_chain_tee_islice.py
# chain, tee, islice examples

from itertools import chain, tee, islice

a = [1,2,3]
b = ['a','b']

# chain: iterate multiple iterables as one
print("Chained:", list(chain(a, b)))

# tee: create independent iterators (careful with memory)
it1, it2 = tee(range(5), 2)
print("tee it1 first 3:", list(islice(it1, 3)))
print("tee it2 all:", list(it2))

# islice: slice an iterator lazily
print("islice 1..10 step 2:", list(islice(range(1, 11), 0, None, 2)))
