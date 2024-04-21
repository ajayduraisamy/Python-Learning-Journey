# 03_timedelta_future_past.py
# timedelta for future and past dates

from datetime import datetime, timedelta

today = datetime.now()
future = today + timedelta(days=10)
past = today - timedelta(days=30)

print("Today:", today)
print("10 days later:", future)
print("30 days before:", past)
