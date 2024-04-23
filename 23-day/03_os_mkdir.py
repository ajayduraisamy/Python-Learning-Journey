# 03_os_mkdir.py
# Create and remove directories

import os

os.makedirs("test_folder", exist_ok=True)
print("Created folder: test_folder")

os.rmdir("test_folder")
print("Removed folder: test_folder")
