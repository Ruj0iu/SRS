# bob_server.py

import socket
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA1
from time import sleep

CA_HOST = 'ca'
CA_PORT = 65431  # Different port for fetching CA's public key
LISTEN_PORT = 65432

sleep(8)  # Allow time for tcpdump to start

# Step 1: Get CA's public key (needed to verify certificates)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((CA_HOST, CA_PORT))
    ca_public_key = RSA.import_key(s.recv(2048))
    print(f"🔐 [Bob] Received CA public key {ca_public_key.export_key()} .")

# Step 2: Listen for Alice's message + signature + certificate
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('', LISTEN_PORT))
    s.listen()
    print("📥 [Bob] Listening for message from Alice...")
    conn, _ = s.accept()
    with conn:
        data = conn.recv(8192)
        print(f"📦 [Bob] Received data {data} .")

        # Step 3: Split the received data into parts
        try:
            msg_part, sig_cert_part = data.split(b'---SIGMSG---', 1)
            signature, certificate = sig_cert_part.split(b'---CERT---', 1)
        except ValueError:
            print("❌ [Bob] Invalid message format.")
            exit(2)

        print(f"📨 [Bob] Message: {msg_part.decode()}")

        # Step 4: Verify certificate using CA public key
        try:
            msg_part, sig_cert_part = data.split(b'---SIGMSG---', 1)
            sigmsg, certificate = sig_cert_part.split(b'---CERT---', 1)
            alice_CA_key , ca_signiture=certificate.split(b'---SIGNATURE---',1)
        except ValueError:
            print("❌ [Bob] Invalid message format.")
            exit(3)


        # Step 5: Verify signature of message using Alice’s public key
        try:
            alice_pubkey = RSA.import_key(alice_CA_key)
            key_hash = SHA1.new(alice_pubkey.export_key())
            pkcs1_15.new(ca_public_key).verify(key_hash, ca_signiture)  # This would only work if CA signed cert.


            print("✅ [Bob] Certificate is valid.")
        except (ValueError, TypeError):
            print("❌ [Bob] Invalid Certificate on message.")
            exit(4)
        # finally:
        #     print(f"🔑 [Bob] Alice's public key: {alice_pubkey.export_key()} .")
        #     print(f"🔑 [Bob] Alice's certificate: {certificate} .")
        #     print(f"🔑 [Bob] CA's public key: {ca_public_key.export_key()} .")
        #     print(f"🔑 [Bob] Signature: {signature} .")

        try:
            h=SHA1.new(msg_part)
            pkcs1_15.new(alice_pubkey).verify(h, sigmsg)
            print("✅ [Bob] Signature is valid.")

        except (ValueError, TypeError):
            print("❌ [Bob] Invalid Signiture or message.")
            exit(5)


