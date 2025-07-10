# alice_client.py
import socket
from crypto_utils import generate_rsa_keypair, sign_message
from time import sleep
BOB_SAFE_HOST = 'bob'
SAFE_PORT = 65430
EVE_HOST = 'eve'
EVE_PORT = 65431

# Step 1: Generate key pair
private_key, public_key = generate_rsa_keypair()

sleep(6)  # Ensure tcpdump is ready to capture packets
# Step 2: Send Alice's public key securely to Bob
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((BOB_SAFE_HOST, SAFE_PORT))
    s.sendall(public_key)
    print("🔐 [Alice] Sent public key to Bob via safe connection.")

# Step 3: Sign the message
message = b"Hello Bob!"
signature = sign_message(private_key, message)

# Step 4: Send message and signature via Eve
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((EVE_HOST, EVE_PORT))
    s.sendall(message + b'||' + signature)
    print("✉️ [Alice] Sent signed message to Bob via Eve.")
