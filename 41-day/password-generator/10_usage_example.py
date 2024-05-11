# 10_usage_example.py
# Simple usage examples for manual run

from 01_password_gen import generate_password
from 03_save_password import generate_and_save

print("Example password:", generate_password(8))
print("Generate & save:", generate_and_save("generated/example.txt", length=10))
