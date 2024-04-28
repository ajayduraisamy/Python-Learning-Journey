# 01_get_request.py
# Basic GET request

import requests

url = "https://jsonplaceholder.typicode.com/posts/1"
res = requests.get(url)

print("Status Code:", res.status_code)
print("Response JSON:", res.json())
