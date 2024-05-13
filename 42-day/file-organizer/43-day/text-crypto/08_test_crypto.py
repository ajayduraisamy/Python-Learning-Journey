# 08_test_crypto.py
# Basic tests for encryption/decryption

from 01_crypto import generate_key, encrypt_text, decrypt_text

def test_encrypt_decrypt_roundtrip():
    key = generate_key()
    text = "hello world"
    ct = encrypt_text(key, text)
    pt = decrypt_text(key, ct)
    assert pt == text
