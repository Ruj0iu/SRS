from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Util.Padding import pad, unpad
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
import base64

def generate_rsa_keys():
    key = RSA.generate(1024)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

def encrypt_rsa(public_key, data):
    cipher = PKCS1_OAEP.new(RSA.import_key(public_key))
    return cipher.encrypt(data)

def decrypt_rsa(private_key, encrypted_data):
    cipher = PKCS1_OAEP.new(RSA.import_key(private_key))
    return cipher.decrypt(encrypted_data)

def encrypt_message(key, message):
    cipher = AES.new(key, AES.MODE_ECB)
    padded = pad(message, AES.block_size)
    return base64.b64encode(cipher.encrypt(padded))

def decrypt_message(key, encrypted):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted = cipher.decrypt(base64.b64decode(encrypted))
    return unpad(decrypted, AES.block_size).decode()
