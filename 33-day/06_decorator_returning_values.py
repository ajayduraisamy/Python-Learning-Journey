# 06_decorator_returning_values.py
# Decorator that returns modified output

def double_output(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * 2
    return wrapper

@double_output
def get_number():
    return 10

print("Modified result:", get_number())
