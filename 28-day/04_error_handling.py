# 04_error_handling.py
# Handling request errors

import requests

try:
    res = requests.get("https://wrong-url-example123.com", timeout=3)
    res.raise_for_status()
except requests.exceptions.RequestException as e:
    print("Error:", e)
