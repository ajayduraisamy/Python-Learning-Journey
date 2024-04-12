# 02_dict_keys_values_items.py
# keys(), values(), items()

student = {
    "name": "Kumar",
    "dept": "CSE",
    "year": 3
}

print("Keys:", student.keys())
print("Values:", student.values())

print("Items:")
for k, v in student.items():
    print(k, ":", v)
