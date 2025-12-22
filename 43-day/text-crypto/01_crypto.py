# 01_crypto.py
# AES-style encryption/decryption using PyCryptodome (AES-CBC + PKCS7)
# Outputs ciphertext as base64 string (IV + ciphertext)

import os
import base64
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

BLOCK_SIZE = 16  # AES block size

def pkcs7_pad(data: bytes) -> bytes:
    pad_len = BLOCK_SIZE - (len(data) % BLOCK_SIZE)
    return data + bytes([pad_len]) * pad_len

def pkcs7_unpad(data: bytes) -> bytes:
    if not data:
        return b""
    pad_len = data[-1]
    if pad_len < 1 or pad_len > BLOCK_SIZE:
        raise ValueError("Invalid padding")
    return data[:-pad_len]

def generate_key(length: int = 32) -> bytes:
    """
    Generate a random key. Default 32 bytes (AES-256).
    """
    return get_random_bytes(length)

def encrypt_text(key: bytes, plaintext: str) -> str:
    """
    Encrypt plaintext (utf-8) and return base64 string containing IV + ciphertext.
    """
    iv = get_random_bytes(BLOCK_SIZE)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    raw = plaintext.encode("utf-8")
    padded = pkcs7_pad(raw)
    ct = cipher.encrypt(padded)
    combined = iv + ct
    return base64.b64encode(combined).decode("utf-8")

def decrypt_text(key: bytes, b64_cipher: str) -> str:
    """
    Decrypt base64-encoded (IV + ciphertext) and return plaintext string.
    """
    combined = base64.b64decode(b64_cipher.encode("utf-8"))
    if len(combined) < BLOCK_SIZE:
        raise ValueError("Ciphertext too short")
    iv = combined[:BLOCK_SIZE]
    ct = combined[BLOCK_SIZE:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded = cipher.decrypt(ct)
    raw = pkcs7_unpad(padded)
    return raw.decode("utf-8")
