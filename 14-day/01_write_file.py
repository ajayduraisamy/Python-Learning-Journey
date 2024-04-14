# 01_write_file.py
# Writing to file

with open("sample.txt", "w") as f:
    f.write("Hello, this is Day 14 file handling test.\n")
    f.write("Writing data to file.\n")

print("File written successfully!")
