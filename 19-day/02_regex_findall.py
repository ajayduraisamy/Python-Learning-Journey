# 02_regex_findall.py
# findall() example

import re

text = "Emails: ajay@test.com, kumar@gmail.com, raj@yahoo.com"

emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z]+\.[a-zA-Z]+", text)
print("Emails found:", emails)
