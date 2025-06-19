# alice_client.py
import socket
from crypto_utils import encrypt_message
from crypto_utils import Secret_Key  # Import the shared key function

HOST = 'localhost'
PORT = 65432

# Same secret key as Bob's
shared_key = Secret_Key()
print("🔑 Shared secret key for encryption:", shared_key.hex())

message = b"Hello Bob! It's Alice, encrypted."

encrypted = encrypt_message(shared_key, message)
print("📤 Sending encrypted message:", encrypted)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))
    client.sendall(encrypted)
