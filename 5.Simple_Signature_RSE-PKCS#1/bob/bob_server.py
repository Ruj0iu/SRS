# bob_server.py
import socket
from crypto_utils import verify_signature

SAFE_PORT = 65430
MESSAGE_PORT = 65432
HOST='0.0.0.0'
# Step 1: Receive Alice's public key securely
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, SAFE_PORT))
    s.listen(1)
    print("🔒 [Bob] Waiting for Alice's public key...")
    conn, _ = s.accept()
    print(f"[Bob] Connection established with Alice --> {_}")
    with conn:
        alice_pub_key = conn.recv(2048)
        print(f"✅ [Bob] Received Alice's public key {alice_pub_key}")

# Step 2: Receive message and signature via Eve
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, MESSAGE_PORT))
    s.listen(1)
    print("📨 [Bob] Waiting for messages from Alice...")
    conn, _ = s.accept()
    print(f"[Bob] Connection established with Eve --> {_}")
    with conn:
        data = conn.recv(4096)
        message, signature = data.split(b'||')
        print(f"📩 [Bob] Received message: {message.decode()}")

        if verify_signature(alice_pub_key, message, signature):
            print("✅ [Bob] Signature is valid!")
        else:
            print("❌ [Bob] Signature verification failed.")
