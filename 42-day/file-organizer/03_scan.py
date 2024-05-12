# 03_scan.py
# Scan directory and return list of files

import os

def scan_files(path):
    if not os.path.exists(path):
        return []
    return [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
