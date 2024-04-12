# 04_nested_dict_access.py
# Working with nested dictionaries

users = {
    "user1": {"name": "Ajay", "role": "Admin"},
    "user2": {"name": "Kumar", "role": "Editor"},
    "user3": {"name": "Raj", "role": "Viewer"}
}

print("User1 name:", users["user1"]["name"])
print("User3 role:", users["user3"]["role"])

# Changing nested value
users["user2"]["role"] = "Admin"
print("Updated:", users)
