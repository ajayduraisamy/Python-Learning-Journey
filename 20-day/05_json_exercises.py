# 05_json_exercises.py
# JSON exercises

import json

# 1. Convert list -> JSON
data = ["python", "js", "java"]
print("List to JSON:", json.dumps(data))

# 2. Validate key inside JSON
emp = {"id": 101, "name": "Raj"}
print("Has name key?", "name" in emp)

# 3. Parse nested JSON
nested = '{"student": {"name": "Ajay", "grade": "A"}}'
obj = json.loads(nested)
print("Student name:", obj["student"]["name"])
