# 11_filter_strings.py
# Filter only strings from mixed list using comprehension

items = [1, "hello", 5.6, "ajay", True, "python"]
strings = [x for x in items if isinstance(x, str)]
print(strings)
