# alice.py
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
import socket
from time import sleep

print("👋 [Alice] Starting Alice's client...")
# Step 1: Receive Bob’s public key
sleep(15)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(("bob", 65433))  # 'bob' is Docker service name
    public_key_data = s.recv(1024)
    print("🔑 [Alice] Received Bob's public key:", public_key_data)
    sleep(2)
    

public_key = RSA.import_key(public_key_data)
cipher = PKCS1_OAEP.new(public_key)

message = b"Hello Bob!"
encrypted_message = cipher.encrypt(message)

# Step 2: Send encrypted message to Bob (via Eve)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(("eve", 65431))  # 'eve' is the proxy
    s.sendall(encrypted_message)
    print("🔒 [Alice] Sent encrypted message to Bob via Eve.")
    sleep(5)
    
    
