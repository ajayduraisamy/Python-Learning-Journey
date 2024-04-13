# 01_args.py
# Functions with *args (multiple arguments)

def add_all(*nums):
    total = 0
    for n in nums:
        total += n
    return total

print("Sum:", add_all(10, 20, 30))
