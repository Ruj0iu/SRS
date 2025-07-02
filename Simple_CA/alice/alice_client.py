#alice_client.py
import socket
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA1
from time import sleep

CA_HOST = 'ca'
CA_PORT = 65430
BOB_HOST = 'bob'
BOB_PORT = 65432

sleep(9)  # Allow time for tcpdump to start

# Step 1: Generate Alice's RSA key pair
key = RSA.generate(2048)
private_key = key
public_key = key.publickey().export_key()

# Step 2: Send public key to CA to get certificate
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((CA_HOST, CA_PORT))
    s.sendall(public_key)
    certificate = s.recv(4096)
    print("✅ [Alice] Received certificate from CA.")

# Step 3: Sign the message using Alice's private key
message = b"Hello Bob!"
hash_msg = SHA1.new(message)
signature = pkcs1_15.new(private_key).sign(hash_msg)
print("✍️ [Alice] Signed the message.")



# Step 4: Send message + signature + certificate to Bob
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((BOB_HOST, BOB_PORT))
    s.sendall(message + b'---SIGMSG---' + signature + b'---CERT---' + certificate)
    print("📨 [Alice] Sent message, signature and certificate to Bob.")
