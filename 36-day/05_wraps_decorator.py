# 05_wraps_decorator.py
# functools.wraps preserves original function metadata

from functools import wraps

def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Running:", func.__name__)
        return func(*args, **kwargs)
    return wrapper

@logger
def greet(name):
    return f"Hello {name}"

print(greet("Ajay"))
print("Function name preserved:", greet.__name__)
