# 02_os_listdir.py
# List files and folders

import os

print("Directory contents:")
for item in os.listdir():
    print(item)
