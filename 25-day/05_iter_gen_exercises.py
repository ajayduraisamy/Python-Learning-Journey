# 05_iter_gen_exercises.py
# Practice tasks for iterators & generators

# 1. Generator for even numbers
def even_generator(limit):
    for i in range(limit + 1):
        if i % 2 == 0:
            yield i

print("Even numbers:", list(even_generator(10)))

# 2. Fibonacci generator
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print("Fibonacci 10:", list(fib(10)))
