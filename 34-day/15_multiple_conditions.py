# 15_multiple_conditions.py
# Numbers divisible by 4 and 6 but not 8

result = [x for x in range(1,101) if x % 4 == 0 and x % 6 == 0 and x % 8 != 0]
print(result)
