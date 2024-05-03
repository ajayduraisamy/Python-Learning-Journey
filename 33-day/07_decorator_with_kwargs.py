# 07_decorator_with_kwargs.py
# Decorator handling keyword arguments

def log_kwargs(func):
    def wrapper(**kwargs):
        print("KWARGS passed:", kwargs)
        return func(**kwargs)
    return wrapper

@log_kwargs
def display(name=None, age=None):
    print(f"Name: {name}, Age: {age}")

display(name="Ajay", age=22)
