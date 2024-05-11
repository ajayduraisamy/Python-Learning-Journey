# 02_utils.py
# Helper utilities for CLI and file operations

import os

def save_to_file(path, content):
    dirpath = os.path.dirname(path)
    if dirpath and not os.path.exists(dirpath):
        os.makedirs(dirpath, exist_ok=True)
    with open(path, "a", encoding="utf-8") as f:
        f.write(content + "\\n")

def read_file(path):
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]
