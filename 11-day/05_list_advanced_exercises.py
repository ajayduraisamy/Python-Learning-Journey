# 05_list_advanced_exercises.py
# Harder list practices

nums = [3, 6, 2, 9, 1, 8]

# 1. Square each number
squares = [n*n for n in nums]

# 2. Filter numbers > 5
filtered = [n for n in nums if n > 5]

# 3. Sort filtered list
filtered_sorted = sorted(filtered)

print("Squares:", squares)
print("Filtered >5:", filtered)
print("Filtered sorted:", filtered_sorted)
