# 08_complex_comprehension.py
# Complex multi-condition comprehension

nums = range(1,51)
result = [x for x in nums if x % 3 == 0 and x % 5 != 0 and x % 7 != 0]
print(result)
