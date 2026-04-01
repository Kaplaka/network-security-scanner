import socket
import pickle
from datetime import datetime
from crypto.hybrid import encrypt_message, decrypt_message
from crypto.rsa import generate_keys

HOST = "127.0.0.1"
PORT = 5000

def now():
    return datetime.now().strftime("%H:%M")

def main():
    username = input("Enter your name: ")

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    server_public_key = pickle.loads(client.recv(4096))

    public_key, private_key = generate_keys()
    client.send(pickle.dumps(public_key))

    print("Secure chat started\n")

    while True:
        message = input(f"[{now()}] {username}: ")

        encrypted_key, encrypted_message = encrypt_message(
            message,
            server_public_key
        )

        client.send(pickle.dumps((encrypted_key, encrypted_message)))

        data = client.recv(4096)

        encrypted_key, encrypted_message = pickle.loads(data)

        reply = decrypt_message(
            encrypted_key,
            encrypted_message,
            private_key
        )

        print(f"[{now()}] Server: {reply}")

if __name__ == "__main__":
    main()
