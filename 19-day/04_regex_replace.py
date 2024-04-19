# 04_regex_replace.py
# sub() replace example

import re

text = "Python is awesome. Python is powerful."

new_text = re.sub(r"Python", "AI", text)

print("Before:", text)
print("After:", new_text)
