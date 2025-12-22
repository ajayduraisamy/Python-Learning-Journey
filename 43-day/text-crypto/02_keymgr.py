# 02_keymgr.py
# Simple key management utilities: save & load raw key bytes to file (base64)

import os
import base64

def save_key(path: str, key: bytes):
    folder = os.path.dirname(path)
    if folder and not os.path.exists(folder):
        os.makedirs(folder, exist_ok=True)
    with open(path, "wb") as f:
        f.write(base64.b64encode(key))

def load_key(path: str) -> bytes:
    if not os.path.exists(path):
        raise FileNotFoundError("Key file not found: " + path)
    with open(path, "rb") as f:
        b64 = f.read().strip()
    return base64.b64decode(b64)
