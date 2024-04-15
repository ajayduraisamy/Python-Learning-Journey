# 01_basic_try_except.py
# simple try-except

try:
    num = int("abc")  # error
except ValueError:
    print("Invalid number!")
