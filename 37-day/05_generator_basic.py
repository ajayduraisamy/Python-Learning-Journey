# 05_generator_basic.py
# Basic generator with yield

def counter():
    for i in range(1, 6):
        yield i

gen = counter()
print(list(gen))
