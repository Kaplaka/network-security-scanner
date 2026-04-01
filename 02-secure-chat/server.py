import socket
import pickle
from datetime import datetime
from crypto.hybrid import decrypt_message, encrypt_message
from crypto.rsa import generate_keys

HOST = "127.0.0.1"
PORT = 5000

def now():
    return datetime.now().strftime("%H:%M")

def main():
    public_key, private_key = generate_keys()

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(1)

    print(f"Secure server listening on {HOST}:{PORT}...")

    conn, addr = server.accept()
    print(f"Connected by {addr}")

    conn.send(pickle.dumps(public_key))
    client_public_key = pickle.loads(conn.recv(4096))

    username = "Server"

    while True:
        data = conn.recv(4096)
        if not data:
            break

        encrypted_key, encrypted_message = pickle.loads(data)

        message = decrypt_message(
            encrypted_key,
            encrypted_message,
            private_key
        )

        print(f"[{now()}] Client: {message}")

        reply = input(f"[{now()}] {username}: ")

        encrypted_key, encrypted_message = encrypt_message(
            reply,
            client_public_key
        )

        conn.send(pickle.dumps((encrypted_key, encrypted_message)))

    conn.close()

if __name__ == "__main__":
    main()
