#ca_server.py

import socket
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA1

HOST = ''       # Bind to all interfaces
PORT = 65430    # Registration port
PUB_PORT = 65431  # Port to fetch CA's public key

print("🔌 [CA] Starting Certificate Authority server...")

# Generate CA key pair (you could also save/load if preferred)
ca_key = RSA.generate(2048)
ca_public_key = ca_key.publickey().export_key()
print("🔐 [CA] Key pair generated.")

def sign_certificate(client_pubkey_bytes):
    """Sign the client's public key using CA private key (simulate certificate)."""
    pub_key = RSA.import_key(client_pubkey_bytes)
    hash_pub = SHA1.new(pub_key.export_key())
    signature = pkcs1_15.new(ca_key).sign(hash_pub)
    print(f"[CA] signiture is {signature} .")
    return pub_key.export_key(), signature


# Separate socket to allow Bob to get CA's public key
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PUB_PORT))
    s.listen()
    print("📡 [CA] Serving public key to verifier...")

    conn, addr = s.accept()
    with conn:
        print(f"📡 [CA] Public key request from {addr}")
        conn.sendall(ca_public_key)
        print(f"✅ [CA] Sent CA public key to {addr} .")

# Thread or sequential: registration server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("📩 [CA] Listening for certificate requests...")

    conn, addr = s.accept()
    with conn:
        print(f"🖋️ [CA] Received connection from {addr}")
        client_pubkey = conn.recv(2048)
        cert, signature = sign_certificate(client_pubkey)
        # Send certificate and signature (concatenated)
        conn.sendall(cert + b'---SIGNATURE---' + signature)
        print(f"📨 [CA] Sent signed certificate to {addr} .")


