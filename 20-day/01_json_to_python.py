# 01_json_to_python.py
# Convert JSON string to Python object

import json

data = '{"name": "Ajay", "age": 22, "city": "Chennai"}'

py_data = json.loads(data)  # json -> python
print("Python object:", py_data)
