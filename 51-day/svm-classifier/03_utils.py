# 03_utils.py
# Save metrics helper

import os

def save_metrics(path, text):
    folder = os.path.dirname(path)
    if folder and not os.path.exists(folder):
        os.makedirs(folder, exist_ok=True)
    with open(path, "w") as f:
        f.write(text)
