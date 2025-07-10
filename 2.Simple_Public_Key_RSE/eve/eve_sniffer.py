# eve_sniffer.py
import socket
from time import sleep

print("👋 [Eve] Starting Eve's sniffer...")
# MITM Proxy
eve_host = "0.0.0.0"
eve_port = 65431
bob_host = "bob"
bob_port = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((eve_host, eve_port))
    s.listen()
    print("🔎 [Eve] Waiting for Alice's encrypted message...")
    conn_from_alice, _ = s.accept()
    with conn_from_alice:
        data = conn_from_alice.recv(4096)
        print(f"🛑 [Eve] Intercepted encrypted message: {data}")
        sleep(2)

        # Save intercepted message
        with open("intercepted_publickey.bin", "wb") as f:
            f.write(data)

        # Forward to Bob
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as to_bob:
            to_bob.connect((bob_host, bob_port))
            to_bob.sendall(data)
            to_bob.close()
            print("➡️ [Eve] Forwarded message to Bob.")
            sleep(2)
