import socket
from time import sleep



from crypto_utils import encrypt_message
from crypto_utils import pad_key

HOST = 'eve'  # Eve is the man-in-the-middle
PORT = 65431  # Eve's port
KEY = b'key1'


sleep(3)  # wait for Bob to be ready
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    message = b'Hello Bob!'
    encrypted = encrypt_message(KEY, message)
    s.sendall(encrypted)
    print(f"📤 [Alice] Sent encrypted message: {encrypted}")
    print("🔑 Alice's secret key for encryption:", pad_key(KEY))
