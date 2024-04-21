# 05_datetime_exercises.py
# Practice tasks

from datetime import datetime, timedelta

# 1. Find age from birth year
birth_year = 2000
current_year = datetime.now().year
age = current_year - birth_year
print("Age:", age)

# 2. Date after 100 days
future_100 = datetime.now() + timedelta(days=100)
print("100 days later:", future_100.strftime("%d-%m-%Y"))

# 3. Check if current time is AM or PM
if datetime.now().hour < 12:
    print("It's AM")
else:
    print("It's PM")
