# 01_csv_write.py
# Writing CSV file

import csv

data = [
    ["name", "age", "city"],
    ["Ajay", 22, "Chennai"],
    ["Kumar", 25, "Bangalore"]
]

with open("users.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)

print("CSV written successfully!")
