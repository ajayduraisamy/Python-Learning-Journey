# 03_try_except_finally.py
# try-except-finally example

try:
    file = open("unknown.txt", "r")
except FileNotFoundError:
    print("File not found!")
finally:
    print("This will always run.")
