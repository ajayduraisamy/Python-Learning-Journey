# 01_core.py
# Core logic for organizing files by extension

import os
import shutil
from .config import EXTENSION_MAP

def ensure_folder(path):
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)

def organize_files(base_path):
    if not os.path.exists(base_path):
        print("Base folder not found:", base_path)
        return

    for filename in os.listdir(base_path):
        file_path = os.path.join(base_path, filename)

        if os.path.isdir(file_path):
            continue

        ext = filename.split('.')[-1].lower()
        moved = False

        for category, exts in EXTENSION_MAP.items():
            if ext in exts:
                target_folder = os.path.join(base_path, category)
                ensure_folder(target_folder)
                shutil.move(file_path, os.path.join(target_folder, filename))
                moved = True
                break

        if not moved:
            others_path = os.path.join(base_path, "others")
            ensure_folder(others_path)
            shutil.move(file_path, os.path.join(others_path, filename))

if __name__ == "__main__":
    organize_files(".")
