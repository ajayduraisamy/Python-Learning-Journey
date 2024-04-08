# 05_function_exercises.py
# Function exercises

# 1. Find square of a number
def square(n):
    return n * n

print("Square of 6:", square(6))

# 2. Function that checks even/odd
def even_or_odd(num):
    return "Even" if num % 2 == 0 else "Odd"

print("7 is:", even_or_odd(7))

# 3. Function that returns largest of 3
def largest(a, b, c):
    return max(a, b, c)

print("Largest of 10, 3, 9:", largest(10, 3, 9))
