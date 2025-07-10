import socket

eve_host = '0.0.0.0'
eve_port = 65431

bob_host = 'bob'
bob_port = 65432

print("🔌 [Eve] Starting MITM proxy...")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as listener:
    listener.bind((eve_host, eve_port))
    listener.listen(1)
    print("👂 [Eve] Waiting for Alice to connect...")

    conn_from_alice, addr = listener.accept()
    print(f"📡 [Eve] Connected to Alice at {addr}")

    # Create connection to Bob
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as to_bob:
        to_bob.connect((bob_host, bob_port))
        print(f"🔗 [Eve] Connected to Bob at {bob_host}:{bob_port}")

        with conn_from_alice:
            while True:
                data = conn_from_alice.recv(1024)
                if not data:
                    print("❌ [Eve] Alice closed the connection.")
                    break

                print(f"📥 [Eve] Intercepted: {data}")
                
              

                to_bob.sendall(data)
                print("➡️ [Eve] Forwarded to Bob.")
