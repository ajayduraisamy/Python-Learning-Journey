# 05_package_example.py
# Simple package style folder & import demonstration

# Creating a mini package structure:
# utils/
#    __init__.py
#    math_ops.py

import os

os.makedirs("utils", exist_ok=True)

with open("utils/__init__.py", "w") as f:
    f.write("# package init file")

with open("utils/math_ops.py", "w") as f:
    f.write("def triple(n): return n * 3")

# Importing package module
from utils.math_ops import triple
print("Triple 5:", triple(5))
