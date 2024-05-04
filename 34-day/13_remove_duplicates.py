# 13_remove_duplicates.py
# Remove duplicates preserving order using comprehension

nums = [1,2,2,3,4,4,5]
seen = set()
result = [x for x in nums if not (x in seen or seen.add(x))]
print(result)
