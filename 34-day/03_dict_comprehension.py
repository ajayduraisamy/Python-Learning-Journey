# 03_dict_comprehension.py
# Dictionary comprehension

names = ["Ajay", "Kumar", "Suri"]
lengths = {name: len(name) for name in names}
print(lengths)
