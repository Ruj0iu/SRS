import socket
from Crypto.Cipher import AES
import itertools
import string
import sys
from crypto_utils import  pad_key, key_bytes

# Start Eve's server to accept connections from Alice
eve_host = '0.0.0.0'
eve_port = 65431

# Bob's address inside the Docker network
bob_host = 'bob'
bob_port = 65432

print("🔌 [Eve] Starting MITM proxy...")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as listener:
    listener.bind((eve_host, eve_port))
    listener.listen(1)
    print("👂 [Eve] Waiting for Alice to connect...")

    conn_from_alice, addr = listener.accept()
    with conn_from_alice:
        print(f"📡 [Eve] Connection from Alice at {addr}")
        data = conn_from_alice.recv(1024)
        print(f"📥 [Eve] Intercepted encrypted message: {data}")

        # Save encrypted message to file
        with open("intercepted.bin", "wb") as f:
            f.write(data)
        print("💾 [Eve] Saved intercepted message to intercepted.bin")


        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as to_bob:
            to_bob.connect((bob_host, bob_port))
            to_bob.sendall(data)
            print("📤 [Eve] Forwarded message to Bob.")

        


print("✅ [Eve] MITM session complete.")
