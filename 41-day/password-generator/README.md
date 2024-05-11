# Password Generator CLI (Day 41)

Simple CLI tool to generate strong passwords and optionally save them.

Usage:
- Generate a password:
  python -m 04_cli

- Generate with custom length:
  python -m 04_cli --length 16

- Generate and save:
  python -m 04_cli --save

Files:
- 01_password_gen.py  : core logic
- 04_cli.py           : CLI entrypoint
- generated/passwords.txt - saved passwords (created when using --save)
