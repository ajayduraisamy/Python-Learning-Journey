# 05_advanced_error_exercises.py
# Practice problems

# 1. Safe division
def safe_div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero!"

print("Division:", safe_div(10, 0))

# 2. Validate integer input
def safe_int(x):
    try:
        return int(x)
    except ValueError:
        return "Invalid integer!"

print(safe_int("123"))
print(safe_int("xyz"))

# 3. Raise custom error if string is empty
class EmptyStringError(Exception):
    pass

def check_string(s):
    if s == "":
        raise EmptyStringError("String cannot be empty!")

try:
    check_string("")
except EmptyStringError as e:
    print("Caught:", e)
