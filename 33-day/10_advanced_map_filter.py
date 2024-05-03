# 10_advanced_map_filter.py
# Complex map/filter operations combined

nums = list(range(1, 21))

# Square only even numbers
result = list(
    map(lambda x: x * x,
        filter(lambda x: x % 2 == 0, nums))
)

print("Squares of even numbers 1–20:", result)
