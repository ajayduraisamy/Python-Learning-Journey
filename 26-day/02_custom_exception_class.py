# 02_custom_exception_class.py
# Defining your own exception class

class AgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise AgeError("Age must be 18 or above!")
    return "Valid age"

try:
    print(check_age(15))
except AgeError as e:
    print("Error:", e)
