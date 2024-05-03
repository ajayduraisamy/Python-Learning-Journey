# 03_lambda_map_filter_reduce.py
# Lambda, map, filter, reduce examples

from functools import reduce

# Lambda function
square = lambda x: x * x
print("Square 5:", square(5))

# Map -> apply function to all elements
nums = [1, 2, 3, 4]
print("Squares:", list(map(lambda x: x*x, nums)))

# Filter -> keep only even numbers
print("Even:", list(filter(lambda x: x % 2 == 0, nums)))

# Reduce -> sum all elements
print("Sum:", reduce(lambda a, b: a + b, nums))
