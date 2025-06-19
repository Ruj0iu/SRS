# crypto_utils.py
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

BLOCK_SIZE = 16
# Generate shared secret key (AES needs 16/24/32 bytes key)
Secret_Key=b"b0d8a336156e451c5c36aeb9dd88da01"

def pad(data):
    padding_len = BLOCK_SIZE - len(data) % BLOCK_SIZE
    return data + bytes([padding_len]) * padding_len

def unpad(data):
    padding_len = data[-1]
    return data[:-padding_len]

def encrypt_message(key, message):
    cipher = AES.new(key, AES.MODE_ECB)
    padded = pad(message)
    encrypted = cipher.encrypt(padded)
    return base64.b64encode(encrypted)

def decrypt_message(key, encrypted_message):
    cipher = AES.new(key, AES.MODE_ECB)
    decoded = base64.b64decode(encrypted_message)
    decrypted = cipher.decrypt(decoded)
    return unpad(decrypted)
