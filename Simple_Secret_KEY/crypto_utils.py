from Crypto.Cipher import AES
import base64
key_bytes = 4
BLOCK_SIZE = 16
def pad_key(key):
    return key.ljust(BLOCK_SIZE, b'\0')

def encrypt_message(key, message):
    cipher = AES.new(pad_key(key), AES.MODE_ECB)
    return base64.b64encode(cipher.encrypt(message.ljust(16)))

def decrypt_message(key, encrypted):
    cipher = AES.new(pad_key(key), AES.MODE_ECB)
    return cipher.decrypt(base64.b64decode(encrypted)).strip()