# 04_scrape_paragraphs.py
# Extract all paragraphs

import requests
from bs4 import BeautifulSoup

url = "https://example.com"
res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")

paragraphs = soup.find_all("p")

for p in paragraphs:
    print("Paragraph:", p.get_text())
