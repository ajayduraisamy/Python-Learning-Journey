# 05_exception_exercises.py
# small exception handling exercises

# 1. division handler
def safe_div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero!"

print("Division:", safe_div(10, 0))

# 2. convert string to int safely
def safe_int(s):
    try:
        return int(s)
    except:
        return "Invalid integer"

print("Convert '123':", safe_int("123"))
print("Convert 'xyz':", safe_int("xyz"))
