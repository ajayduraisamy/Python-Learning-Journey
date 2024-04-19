# 03_regex_match.py
# match() example

import re

pattern = r"AJAY"

result = re.match(pattern, "AJAY is learning Python")

if result:
    print("Matched:", result.group())
else:
    print("Not matched")
