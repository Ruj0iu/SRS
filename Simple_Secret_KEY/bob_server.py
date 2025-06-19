# bob_server.py
import socket
from crypto_utils import decrypt_message
from crypto_utils import Secret_Key  # Import the shared key function
from Crypto.Random import get_random_bytes

HOST = 'localhost'
PORT = 65432

# Simulate shared secret key (should match Alice’s key)
shared_key = Secret_Key()
print("🔑 Shared secret key for decryption:", shared_key.hex())

# Bob's server to receive encrypted messages from Alice
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen()
    print("🔐 Bob is listening for connections...")

    conn, addr = server.accept()
    with conn:
        print(f"📥 Connected by {addr}")
        encrypted = conn.recv(1024)
        print(f"🔒 Encrypted message received: {encrypted}")

        try:
            decrypted = decrypt_message(shared_key, encrypted)
            print("📬 Decrypted message from Alice:", decrypted.decode())
        except Exception as e:
            print("❌ Failed to decrypt message:", str(e))
