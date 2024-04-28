# 05_requests_exercises.py
# Practice problems

import requests

# 1. Fetch list of posts
posts = requests.get("https://jsonplaceholder.typicode.com/posts").json()
print("Total posts:", len(posts))

# 2. Extract titles only
titles = [p["title"] for p in posts[:5]]
print("First 5 titles:", titles)

# 3. Fetch one user and display its data
user = requests.get("https://jsonplaceholder.typicode.com/users/1").json()
print("User info:", user)
