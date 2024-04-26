# 04_context_manager_error.py
# Using context manager for safe file handling

try:
    with open("unknown.txt") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found - handled safely!")
