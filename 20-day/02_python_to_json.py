# 02_python_to_json.py
# Convert Python object to JSON string

import json

person = {"name": "Kumar", "age": 25, "city": "Bangalore"}

json_data = json.dumps(person, indent=4)  # python -> json
print(json_data)
