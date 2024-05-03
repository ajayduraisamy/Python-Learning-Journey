# 15_filter_complex.py
# Complex filtering using lambda

numbers = list(range(1, 51))

# Keep numbers divisible by both 3 and 5 (i.e., 15)
result = list(filter(lambda x: x % 3 == 0 and x % 5 == 0, numbers))

print("Numbers divisible by 15:", result)
