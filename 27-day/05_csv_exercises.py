# 05_csv_exercises.py
# CSV practice problems

import csv

# 1. Append new row to CSV
with open("users.csv", "a", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Raj", 30, "Hyderabad"])

# 2. Read all names from CSV
names = []
with open("users.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        names.append(row[0])

print("Names:", names)
