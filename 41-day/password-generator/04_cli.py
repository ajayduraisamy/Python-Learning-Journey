# 04_cli.py
# CLI interface for password generator

import argparse
from .01_password_gen import generate_password
from .03_save_password import generate_and_save

def main():
    parser = argparse.ArgumentParser(description="Password Generator CLI")
    parser.add_argument("-l", "--length", type=int, default=12, help="Password length")
    parser.add_argument("--no-symbols", dest="symbols", action="store_false", help="Disable symbols")
    parser.add_argument("--no-numbers", dest="numbers", action="store_false", help="Disable numbers")
    parser.add_argument("--save", action="store_true", help="Save password to file")
    args = parser.parse_args()

    pwd = generate_password(length=args.length, use_symbols=args.symbols, use_numbers=args.numbers)
    print("Generated password:", pwd)

    if args.save:
        path = "generated/passwords.txt"
        generate_and_save(path=path, length=args.length, use_symbols=args.symbols, use_numbers=args.numbers)
        print("Saved to:", path)

if __name__ == "__main__":
    main()
