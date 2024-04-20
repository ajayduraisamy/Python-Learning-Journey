# 04_write_json_file.py
# Writing JSON file

import json

users = [
    {"name": "Ajay", "age": 22},
    {"name": "Suri", "age": 28}
]

with open("users.json", "w") as f:
    json.dump(users, f, indent=4)

print("JSON file written successfully!")
