# 05_decorator_exercises.py
# Decorator practice tasks

# 1. Timer decorator
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Time taken:", end - start)
        return result
    return wrapper

@timer
def slow_add(a, b):
    time.sleep(0.5)
    return a + b

print("Result:", slow_add(5, 10))

# 2. Validator decorator
def validate_positive(func):
    def wrapper(x):
        if x < 0:
            return "Negative numbers not allowed!"
        return func(x)
    return wrapper

@validate_positive
def square(n):
    return n * n

print(square(4))
print(square(-3))
