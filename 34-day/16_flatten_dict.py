# 16_flatten_dict.py
# Flatten a nested dictionary using comprehension

data = {
    "a": {"x": 1, "y": 2},
    "b": {"x": 3, "y": 4}
}

flat = {f"{k}_{subk}": subv for k, v in data.items() for subk, subv in v.items()}
print(flat)
