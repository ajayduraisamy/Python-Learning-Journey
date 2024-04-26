# 03_multiple_errors.py
# Handling multiple exceptions

try:
    a = int("abc")   # ValueError
    b = 10 / 0       # ZeroDivisionError
except (ValueError, ZeroDivisionError) as e:
    print("Caught error:", e)
