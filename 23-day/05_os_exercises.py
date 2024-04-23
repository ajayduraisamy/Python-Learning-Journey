# 05_os_exercises.py
# OS module practice tasks

import os

# 1. Create multiple folders
for i in range(1, 4):
    os.makedirs(f"folder_{i}", exist_ok=True)

# 2. List only directories
dirs = [d for d in os.listdir() if os.path.isdir(d)]
print("Directories:", dirs)

# 3. Delete created folders
for i in range(1, 4):
    os.rmdir(f"folder_{i}")

print("Cleanup completed!")
