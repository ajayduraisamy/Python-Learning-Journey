# 02_format_datetime.py
# Formatting datetime

from datetime import datetime

now = datetime.now()

print(now.strftime("%Y-%m-%d"))
print(now.strftime("%d/%m/%Y"))
print(now.strftime("%I:%M %p"))
print(now.strftime("%A, %B %d %Y"))
