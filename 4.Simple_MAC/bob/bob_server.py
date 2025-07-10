import socket
from crypto_utils import verify_mac

SAFE_NET_PORT = 65430
INSECURE_PORT = 65432
HOST='0.0.0.0'

# Step 1: Receive MAC key securely
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, SAFE_NET_PORT))
    s.listen(1)
    conn, _ = s.accept()
    with conn:
        mac_key = conn.recv(1024)
        print(f"🔑 [Bob] Received MAC key securely: {mac_key}")

# Step 2: Receive message + MAC through Eve
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, INSECURE_PORT))
    s.listen(1)
    conn, _ = s.accept()
    with conn:
        data = conn.recv(4096)
        message, mac = data.split(b'||')
        print(f"📩 [Bob] Received message: {message}")
        print(f"🔐 [Bob] Received MAC: {mac}")

        # Verify
        if verify_mac(mac_key, message, mac):
            print("✅ [Bob] MAC verification passed")
        else:
            print("❌ [Bob] MAC verification failed")
