# 04_os_rename.py
# Rename a file

import os

# Create file
with open("old_file.txt", "w") as f:
    f.write("Temporary file")

# Rename file
os.rename("old_file.txt", "new_file.txt")

print("File renamed to new_file.txt")
