# 02_read_file.py
# Reading from file

with open("sample.txt", "r") as f:
    data = f.read()

print("File content:")
print(data)
