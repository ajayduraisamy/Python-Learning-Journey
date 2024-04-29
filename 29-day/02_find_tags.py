# 02_find_tags.py
# Find tags and extract text

import requests
from bs4 import BeautifulSoup

url = "https://example.com"
res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")

headings = soup.find_all("h1")
print("H1 tags:", headings)

for h in headings:
    print("Text:", h.get_text())
