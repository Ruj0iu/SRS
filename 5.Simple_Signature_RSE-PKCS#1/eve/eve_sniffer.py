# eve_sniffer.py
import socket

EVE_HOST = '0.0.0.0'
EVE_PORT = 65431
BOB_HOST = 'bob'
BOB_PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as listener:
    listener.bind((EVE_HOST, EVE_PORT))
    listener.listen(1)
    print("🕵️ [Eve] Waiting for Alice to send message...")

    conn_from_alice, _ = listener.accept()
    with conn_from_alice:
        data = conn_from_alice.recv(4096)
        print(f"📦 [Eve] Intercepted: {data}")

        # Forward to Bob
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as to_bob:
            to_bob.connect((BOB_HOST, BOB_PORT))
            to_bob.sendall(data)
            print("➡️ [Eve] Forwarded to Bob.")
