# 01_password_gen.py
# Simple password generator logic

import random
import string
from .config import DEFAULT_LENGTH, USE_SYMBOLS, USE_NUMBERS

def generate_password(length=DEFAULT_LENGTH, use_symbols=USE_SYMBOLS, use_numbers=USE_NUMBERS):
    chars = list(string.ascii_letters)
    if use_numbers:
        chars += list(string.digits)
    if use_symbols:
        chars += list("!@#$%^&*()-_=+[]{};:,.<>/?")
    if not chars:
        return ""
    return "".join(random.choice(chars) for _ in range(length))

if __name__ == "__main__":
    print(generate_password())
