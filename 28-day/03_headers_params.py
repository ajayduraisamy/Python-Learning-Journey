# 03_headers_params.py
# GET request with headers + params

import requests

url = "https://jsonplaceholder.typicode.com/comments"

params = {"postId": 1}
headers = {"User-Agent": "AjayPythonClient"}

res = requests.get(url, params=params, headers=headers)

print("Status:", res.status_code)
print("First 2 comments:", res.json()[:2])
