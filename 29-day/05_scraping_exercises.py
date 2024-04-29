# 05_scraping_exercises.py
# Practical scraping tasks

import requests
from bs4 import BeautifulSoup

url = "https://example.com"
res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")

# 1. Extract title
print("Title:", soup.title.string)

# 2. Count all <a> tags
a_tags = soup.find_all("a")
print("Total links:", len(a_tags))

# 3. Print first 3 links
for link in a_tags[:3]:
    print("Link:", link.get("href"))
