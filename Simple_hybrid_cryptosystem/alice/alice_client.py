import socket
from time import sleep
from crypto_utils import encrypt_rsa, encrypt_message
from Crypto.Random import get_random_bytes

BOB_HOST = 'bob'
SAFE_NET_PORT = 65430  # Port for Alice to get the public key from Bob

EVE_HOST = 'eve'
EVE_PORT = 65431  # for secret key


# Step 1: Receive Bob's public key
sleep(10)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((BOB_HOST, SAFE_NET_PORT))
    public_key = s.recv(1024)
    print("🔑 [Alice] Received Bob's public key")

# Step 2: Generate a secret key for AES and send it to Bob encrypted
secret_key = get_random_bytes(16)
encrypted_secret_key = encrypt_rsa(public_key, secret_key)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((EVE_HOST, EVE_PORT))
    s.sendall(encrypted_secret_key)
    print("🔐 [Alice] Sent encrypted secret key to Bob via Eve.")

    # Step 3: Send encrypted message using AES
    sleep(2)  
    message = b"Hello Bob!"
    encrypted_message = encrypt_message(secret_key, message)
    s.sendall(encrypted_message)
    print("✉️ [Alice] Sent encrypted message via Eve.")
