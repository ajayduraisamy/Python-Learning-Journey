# 02_decorator_with_args.py
# Decorator that accepts arguments

def debug(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args}")
        return func(*args, **kwargs)
    return wrapper

@debug
def add(a, b):
    return a + b

print("Result:", add(10, 20))
