# 10_dict_swap.py
# Swap keys and values using dict comprehension

data = {"a": 1, "b": 2, "c": 3}
swapped = {v: k for k, v in data.items()}
print(swapped)
