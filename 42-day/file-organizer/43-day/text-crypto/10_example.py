# 10_example.py
# Example usage script (manual run)

from 01_crypto import generate_key, encrypt_text, decrypt_text
from 02_keymgr import save_key, load_key

print("Generating key...")
k = generate_key()
save_key("keys/example.key", k)
print("Key saved to keys/example.key")

plaintext = "This is a test message."
print("Plaintext:", plaintext)

ct = encrypt_text(k, plaintext)
print("Ciphertext (base64):", ct)

pt = decrypt_text(k, ct)
print("Decrypted:", pt)
