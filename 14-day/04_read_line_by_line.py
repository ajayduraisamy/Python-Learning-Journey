# 04_read_line_by_line.py
# Reading line by line

with open("sample.txt", "r") as f:
    for line in f:
        print("Line:", line.strip())
