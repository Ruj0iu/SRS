import hmac
import hashlib

def generate_mac(key, message):
    return hmac.new(key, message, hashlib.sha1).digest()

def verify_mac(key, message, mac):
    expected_mac = generate_mac(key, message)
    return hmac.compare_digest(expected_mac, mac)