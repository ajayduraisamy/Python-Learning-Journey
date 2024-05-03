# 13_decorator_for_validation.py
# Decorator that validates inputs

def validate_numbers(func):
    def wrapper(a, b):
        if not (isinstance(a, int) and isinstance(b, int)):
            return "Inputs must be integers!"
        return func(a, b)
    return wrapper

@validate_numbers
def divide(a, b):
    return a / b

print(divide(10, 2))
print(divide("x", 5))
