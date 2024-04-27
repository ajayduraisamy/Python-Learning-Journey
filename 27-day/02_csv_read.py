# 02_csv_read.py
# Reading CSV file

import csv

with open("users.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print("Row:", row)
