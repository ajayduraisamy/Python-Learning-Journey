# 05_file_exercises.py
# Small file handling exercises

# 1. Write numbers 1 to 10 in a file
with open("numbers.txt", "w") as f:
    for i in range(1, 11):
        f.write(str(i) + "\n")

# 2. Read numbers and convert to list
with open("numbers.txt", "r") as f:
    nums = [int(line.strip()) for line in f]

print("Numbers list:", nums)
