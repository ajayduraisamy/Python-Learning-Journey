# 01_regex_search.py
# Basic search

import re

text = "My number is 9876543210"

match = re.search(r"\d{10}", text)

if match:
    print("Found number:", match.group())
