# 03_read_json_file.py
# Reading JSON file

import json

sample = {"product": "Laptop", "price": 55000}

# create file
with open("data.json", "w") as f:
    json.dump(sample, f, indent=4)

# read file
with open("data.json", "r") as f:
    data = json.load(f)

print("File JSON:", data)
