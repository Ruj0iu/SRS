# bob.py
from Crypto.PublicKey import RSA
import socket
from time import sleep

print("👋 [Bob] Starting Bob's server...")
# Generate RSA key pair
key = RSA.generate(1024)
private_key = key.export_key()
public_key = key.publickey().export_key()

# Send public key to Alice
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(("0.0.0.0", 65433))
    s.listen()
    print("🔑 [Bob] Waiting for Alice to request public key...")
    sleep(2)  # Wait for Alice to connect
    conn, addr = s.accept()
    with conn:
        conn.sendall(public_key)
        print("✅ [Bob] Sent public key to Alice.")
        sleep(2)

# Listen for encrypted message
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(("0.0.0.0", 65432))
    s.listen()
    print("🔒 [Bob] Waiting for encrypted message from Alice...")

    conn, addr = s.accept()
    with conn:
        encrypted = conn.recv(1024)
        print(f"📩 [Bob] Received encrypted message: {encrypted}")
        sleep(2)
        # Decrypt the message
        from Crypto.Cipher import PKCS1_OAEP
        cipher = PKCS1_OAEP.new(key)
        decrypted = cipher.decrypt(encrypted)
        print(f"🔓 [Bob] Decrypted message: {decrypted.decode()}")
        sleep(2)
