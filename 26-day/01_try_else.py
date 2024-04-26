# 01_try_else.py
# try / except / else block

try:
    num = int("10")
except ValueError:
    print("Invalid number!")
else:
    print("Conversion successful:", num)
