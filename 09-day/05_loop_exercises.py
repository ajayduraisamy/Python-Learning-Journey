# 05_loop_exercises.py
# Loop practice questions

# 1. Sum of numbers 1–20
total = sum(range(1, 21))
print("Sum 1-20:", total)

# 2. Print even numbers from 1–20
print("Even numbers:")
for n in range(1, 21):
    if n % 2 == 0:
        print(n)

# 3. Multiplication table of 7
print("\nMultiplication table of 7:")
for i in range(1, 11):
    print(f"7 x {i} = {7*i}")
