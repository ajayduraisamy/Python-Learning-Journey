# 06_yield_from.py
# Using yield from to delegate generators

def gen1():
    yield from [1, 2, 3]

def gen2():
    yield from ["a", "b", "c"]

def combined():
    yield from gen1()
    yield from gen2()

print(list(combined()))
