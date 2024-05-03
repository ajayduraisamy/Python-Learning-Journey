# 11_decorator_with_return_args.py
# Decorator that logs return values

def log_return(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned:", result)
        return result
    return wrapper

@log_return
def multiply(a, b):
    return a * b

multiply(5, 6)
