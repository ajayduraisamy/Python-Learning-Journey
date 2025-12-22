# 04_cli.py
# CLI interface for encryption/decryption and key management

import argparse
import sys
from 01_crypto import generate_key, encrypt_text, decrypt_text
from 02_keymgr import save_key, load_key
from 03_utils import save_text, read_text

DEFAULT_KEY_PATH = "keys/default.key"

def cmd_gen_key(args):
    key = generate_key()
    path = args.out or DEFAULT_KEY_PATH
    save_key(path, key)
    print("Key generated and saved to:", path)

def cmd_encrypt(args):
    key_path = args.key or DEFAULT_KEY_PATH
    try:
        key = load_key(key_path)
    except Exception as e:
        print("Failed to load key:", e)
        sys.exit(1)
    plaintext = args.text or (read_text(args.infile) if args.infile else "")
    if not plaintext:
        print("No plaintext provided.")
        sys.exit(1)
    ct = encrypt_text(key, plaintext)
    if args.out:
        save_text(args.out, ct)
        print("Ciphertext saved to:", args.out)
    else:
        print("Ciphertext:", ct)

def cmd_decrypt(args):
    key_path = args.key or DEFAULT_KEY_PATH
    try:
        key = load_key(key_path)
    except Exception as e:
        print("Failed to load key:", e)
        sys.exit(1)
    b64_ct = args.text or (read_text(args.infile) if args.infile else "")
    if not b64_ct:
        print("No ciphertext provided.")
        sys.exit(1)
    try:
        pt = decrypt_text(key, b64_ct)
    except Exception as e:
        print("Decryption failed:", e)
        sys.exit(1)
    if args.out:
        save_text(args.out, pt)
        print("Plaintext saved to:", args.out)
    else:
        print("Plaintext:", pt)

def main():
    parser = argparse.ArgumentParser(description="Simple Text Encryption CLI (AES-style)")
    sub = parser.add_subparsers(dest="cmd")

    g = sub.add_parser("gen-key", help="Generate and save a random key")
    g.add_argument("--out", "-o", help="Key output path (base64)")

    e = sub.add_parser("encrypt", help="Encrypt plaintext")
    e.add_argument("--key", "-k", help="Path to key file (base64)")
    e.add_argument("--text", "-t", help="Plaintext to encrypt (mutually exclusive with --infile)")
    e.add_argument("--infile", "-i", help="Read plaintext from file")
    e.add_argument("--out", "-o", help="Write ciphertext to file")

    d = sub.add_parser("decrypt", help="Decrypt ciphertext")
    d.add_argument("--key", "-k", help="Path to key file (base64)")
    d.add_argument("--text", "-t", help="Ciphertext (base64) to decrypt")
    d.add_argument("--infile", "-i", help="Read ciphertext from file")
    d.add_argument("--out", "-o", help="Write plaintext to file")

    args = parser.parse_args()

    if args.cmd == "gen-key":
        cmd_gen_key(args)
    elif args.cmd == "encrypt":
        cmd_encrypt(args)
    elif args.cmd == "decrypt":
        cmd_decrypt(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
