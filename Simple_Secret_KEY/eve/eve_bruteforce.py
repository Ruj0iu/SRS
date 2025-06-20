# eve_bruteforce.py
from Crypto.Cipher import AES
import itertools
import string
import time
from crypto_utils import  pad_key, key_bytes , decrypt_message


def brute_force_key(encrypted_data):
    attempts = 0
    charset = string.printable  # or string.ascii_letters + string.digits
    for key_tuple in itertools.product(charset, repeat=4):
        key_candidate = ''.join(key_tuple).encode()
        
        decrypted = decrypt_message(key_candidate, encrypted_data)
        attempts= attempts + 1
        if decrypted.startswith(b"Hello"):
            print("🎉 Key found:", key_candidate)
            print("📜 Decrypted message:", decrypted)
            print(f"Attempts: {attempts} ---- percentege: {attempts / (2**(key_bytes*8)) * 100:.4f}%")
            return
    print("❌ Key not found.")





time.sleep(3)
# Wait for the file to exist
print("⏳ Waiting for intercepted.bin...")
while True:
    try:
        with open("intercepted.bin", "rb") as f:
            encrypted_data = f.read()
            print("📄 Encrypted data loaded. Starting brute-force...")
            break
    except FileNotFoundError:
        time.sleep(1)

brute_force_key(encrypted_data)
