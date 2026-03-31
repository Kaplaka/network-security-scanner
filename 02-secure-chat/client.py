import socket
import pickle
import sys
from crypto.hybrid import encrypt_message

HOST = "127.0.0.1"
PORT = 5000

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        client.connect((HOST, PORT))
    except ConnectionRefusedError:
        print("Error: Could not connect to server. Is it running?")
        return

    # Recevoir la clé publique du serveur
    print("Waiting for public key...")
    public_key = pickle.loads(client.recv(4096))

    print("Connected to secure server.")
    print("Type messages (Type 'quit' to exit)\n")

    while True:
        try:
            message = input("You: ")
            if message.lower() == 'quit':
                break
            if not message:
                continue

            # Chiffrement hybride
            encrypted_key, encrypted_message = encrypt_message(message, public_key)
            
            # Envoi
            data = pickle.dumps((encrypted_key, encrypted_message))
            client.send(data)
            
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"Error: {e}")
            break

    client.close()

if __name__ == "__main__":
    main()
