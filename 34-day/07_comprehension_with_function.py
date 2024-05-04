# 07_comprehension_with_function.py
# Using a function inside comprehension

def double(x): return x*2

nums = [1,2,3,4,5]
result = [double(x) for x in nums]
print(result)
