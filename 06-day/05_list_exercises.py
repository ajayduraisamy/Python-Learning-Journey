# 05_list_exercises.py
# advanced list practice

nums = [5, 10, 15, 20, 25]

# double each number
doubled = [n * 2 for n in nums]

# filter numbers > 10
filtered = [n for n in nums if n > 10]

print("Original:", nums)
print("Doubled:", doubled)
print("Filtered:", filtered)
