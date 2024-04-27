# 04_dict_reader.py
# Reading CSV using DictReader

import csv

with open("users_dict.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["name"], "-", row["city"])
