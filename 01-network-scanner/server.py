import socket
import pickle
from crypto.hybrid import decrypt_message
from crypto.rsa import generate_keys

HOST = "127.0.0.1"
PORT = 5000

def main():
    # Generate RSA keys
    public_key, private_key = generate_keys()

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(1)

    print(f"Server listening on {HOST}:{PORT}...")

    conn, addr = server.accept()
    print(f"Connected by {addr}")

    # Send public key to client
    conn.send(pickle.dumps(public_key))

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

        print("Client:", message)

    conn.close()

if __name__ == "__main__":
    main()
