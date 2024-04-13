# 05_function_exercises.py
# Advanced function exercises

# 1. Largest using *args
def largest(*nums):
    return max(nums)

print("Largest:", largest(10, 3, 50, 7))

# 2. Repeat string n times using lambda
repeat = lambda text, n: text * n
print(repeat("Hi ", 3))

# 3. Recursion: sum of numbers 1..n
def sum_rec(n):
    if n == 1:
        return 1
    return n + sum_rec(n - 1)

print("Sum 1-10:", sum_rec(10))
