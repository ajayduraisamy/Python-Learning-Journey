# 03_dict_comprehension.py
# Dictionary comprehension examples

nums = [1, 2, 3, 4, 5]

# square each number
squares = {n: n*n for n in nums}

# number -> even/odd
status = {n: ("even" if n % 2 == 0 else "odd") for n in nums}

print("Squares:", squares)
print("Status:", status)
