# 08_infinite_generators.py
# Infinite generator (careful!)

def infinite_counter(start=0):
    while True:
        yield start
        start += 1

gen = infinite_counter()
print(next(gen), next(gen), next(gen), next(gen))
