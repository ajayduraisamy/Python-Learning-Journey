# 01_current_datetime.py
# Current date and time

from datetime import datetime

now = datetime.now()
print("Current DateTime:", now)
print("Date:", now.date())
print("Time:", now.time())
