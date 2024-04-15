# 02_multiple_except.py
# multiple except blocks

try:
    a = 10
    b = 0
    print(a / b)
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    print("Error:", e)
