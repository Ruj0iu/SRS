# bob.py
import socket
from crypto_utils import generate_rsa_keys,decrypt_rsa ,encrypt_message, decrypt_message
from time import sleep

HOST = '0.0.0.0'
PORT = 65432
SAFE_NET_PORT = 65430  # Port for Alice to get the public key from Bob

# Generate RSA key pair
PRIVATE_KEY, PUBLIC_KEY = generate_rsa_keys()

sleep(3)  # Allow time for Alice to connect

# 1. Wait for Alice to request public key
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, SAFE_NET_PORT))
    s.listen(1)
    print("🔑 [Bob] Waiting for Alice to request public key...")
    conn, _ = s.accept()
    with conn:
        conn.sendall(PUBLIC_KEY)
        print("✅ [Bob] Sent public key to Alice.")
       

# 2. Receive encrypted secret key from Eve
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    print("🔒 [Bob] Waiting for encrypted secret key from Alice...")
    conn, _ = s.accept()
    with conn:
        encrypted_secret_key = conn.recv(1024)
        print(encrypted_secret_key)
        secret_key = decrypt_rsa(PRIVATE_KEY, encrypted_secret_key)
        print("🔓 [Bob] Secured  secret key.")

# 3. Receive encrypted message
        print("📨 [Bob] Waiting for encrypted message...")
        encrypted_message = conn.recv(1024)
        message = decrypt_message(secret_key, encrypted_message)
        print(f"📬 [Bob] Received message: {message}")
