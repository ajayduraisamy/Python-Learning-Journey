# Text Encryption CLI (Day 43)

A simple AES-style encryption/decryption CLI using PyCryptodome (AES-CBC + PKCS7 padding).

## Install
pip install -r requirements.txt

## Generate a key
python -m 04_cli gen-key --out keys/my.key

## Encrypt plaintext
# inline text
python -m 04_cli encrypt -k keys/my.key -t "secret message"

# from file, save ciphertext
python -m 04_cli encrypt -k keys/my.key -i secret.txt -o secret.ct

## Decrypt ciphertext
python -m 04_cli decrypt -k keys/my.key -t "<base64-ciphertext>"
python -m 04_cli decrypt -k keys/my.key -i secret.ct -o secret_plain.txt

## Notes
- Keys are stored as base64 in the key file.
- Ciphertext is base64(IV + ciphertext) to allow easy storage/transfer.
