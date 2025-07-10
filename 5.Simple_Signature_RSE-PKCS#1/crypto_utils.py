# crypto_utils.py
from Crypto.Signature import pkcs1_15
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA1

def generate_rsa_keypair():
    key = RSA.generate(1024)
    return key.export_key(), key.publickey().export_key()

def sign_message(private_key_bytes, message):
    key = RSA.import_key(private_key_bytes)
    h = SHA1.new(message)
    signature = pkcs1_15.new(key).sign(h)
    return signature

def verify_signature(public_key_bytes, message, signature):
    key = RSA.import_key(public_key_bytes)
    h = SHA1.new(message)
    try:
        pkcs1_15.new(key).verify(h, signature)
        return True
    except (ValueError, TypeError):
        return False
