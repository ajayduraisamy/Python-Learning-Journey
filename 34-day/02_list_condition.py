# 02_list_condition.py
# Conditional comprehension

nums = range(1,21)
evens = [x for x in nums if x % 2 == 0]
print(evens)
