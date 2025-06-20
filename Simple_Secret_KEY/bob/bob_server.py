# bob_server.py

import socket
from crypto_utils import decrypt_message
from crypto_utils import pad_key
from time import sleep

HOST = '0.0.0.0'
PORT = 65432
KEY = b'key1'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    print("📥 Bob waiting for message...")
    conn, addr = s.accept()
    with conn:
        data = conn.recv(1024)
        print(f"🔒[Bob] Encrypted message received: {data}")
        decrypted = decrypt_message(KEY, data)
        print(f"📬[Bob] Decrypted message from Alice: {decrypted}")
        print("🔑[Bob] Bob's secret key for encryption:", pad_key(KEY))
