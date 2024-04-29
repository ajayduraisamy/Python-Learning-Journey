# 03_extract_links.py
# Extract all hyperlinks

import requests
from bs4 import BeautifulSoup

url = "https://example.com"
res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")

links = soup.find_all("a")

for link in links:
    print("Link:", link.get("href"))
