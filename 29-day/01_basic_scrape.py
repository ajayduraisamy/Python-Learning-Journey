# 01_basic_scrape.py
# Basic web scraping with BeautifulSoup

import requests
from bs4 import BeautifulSoup

url = "https://example.com"
res = requests.get(url)

soup = BeautifulSoup(res.text, "html.parser")

print("Title:", soup.title.string)
