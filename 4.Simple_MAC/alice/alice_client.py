import socket
from time import sleep
from crypto_utils import generate_mac

BOB_HOST = 'bob'
SAFE_NET_PORT = 65430
EVE_HOST = 'eve'
MITM_PORT = 65431

# Shared MAC key
mac_key = b'securemackey42'
sleep(6) # Wait for tcpdump to start
# Step 1: Send MAC key over secure port
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((BOB_HOST, SAFE_NET_PORT))
    s.sendall(mac_key)
    print("🔑 [Alice] Sent MAC key securely to Bob")

sleep(1)

# Step 2: Send message + MAC via Eve
message = b"Hello Bob!"
mac = generate_mac(mac_key, message)

# Send both message and MAC through Eve
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((EVE_HOST, MITM_PORT))
    s.sendall(message + b'||' + mac)
    print("✉️ [Alice] Sent message and MAC via Eve")
