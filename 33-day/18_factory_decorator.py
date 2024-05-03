# 18_factory_decorator.py
# Decorator factory (decorator with arguments)

def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet():
    print("Hello Ajay!")

greet()
