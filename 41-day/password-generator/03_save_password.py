# 03_save_password.py
# Small wrapper to generate and save passwords

from .01_password_gen import generate_password  # relative import
from .02_utils import save_to_file

def generate_and_save(path="generated/passwords.txt", length=12, use_symbols=True, use_numbers=True):
    pwd = generate_password(length, use_symbols, use_numbers)
    save_to_file(path, pwd)
    return pwd

if __name__ == "__main__":
    print(generate_and_save())
