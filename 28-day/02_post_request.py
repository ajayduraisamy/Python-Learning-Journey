# 02_post_request.py
# POST request example

import requests

url = "https://jsonplaceholder.typicode.com/posts"
payload = {"title": "Ajay Post", "body": "Learning Python", "userId": 1}

res = requests.post(url, json=payload)

print("Status:", res.status_code)
print("Response:", res.json())
