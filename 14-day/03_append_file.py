# 03_append_file.py
# Appending to file

with open("sample.txt", "a") as f:
    f.write("Appending new line from Day 14.\n")

print("Data appended into file!")
