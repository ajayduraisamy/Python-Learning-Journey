# 03_dict_writer.py
# Writing CSV using DictWriter

import csv

data = [
    {"name": "Ajay", "age": 22, "city": "Chennai"},
    {"name": "Suri", "age": 28, "city": "Coimbatore"}
]

with open("users_dict.csv", "w", newline="") as f:
    fieldnames = ["name", "age", "city"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

print("Dict CSV written!")
