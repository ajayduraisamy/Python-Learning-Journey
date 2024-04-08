# 05_loop_exercises.py
# Mini loop exercises

# 1. Sum of numbers 1-10
total = 0
for i in range(1, 11):
    total += i
print("Sum 1-10:", total)

# 2. Print even numbers from 1-20
evens = [n for n in range(1, 21) if n % 2 == 0]
print("Even numbers:", evens)

# 3. Multiplication table of 5
for i in range(1, 11):
    print(f"5 x {i} = {5*i}")
