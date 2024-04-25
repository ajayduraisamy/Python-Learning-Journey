# 03_generator_function.py
# Generator using yield

def generate_numbers():
    yield 1
    yield 2
    yield 3

for n in generate_numbers():
    print(n)
