# 04_raise_exception.py
# raising custom exception

def check_age(age):
    if age < 18:
        raise ValueError("Age must be 18+")
    print("Valid age:", age)

try:
    check_age(15)
except ValueError as e:
    print("Error:", e)
