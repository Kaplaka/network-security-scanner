import socket
import pickle
from crypto.hybrid import decrypt_message
from crypto.rsa import generate_keys

HOST = "127.0.0.1"
PORT = 5000

def main():
    # 1. Générer les clés RSA au démarrage
    public_key, private_key = generate_keys()

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Permet de relancer vite le serveur
    server.bind((HOST, PORT))
    server.listen(1)

    print(f"Server listening on {HOST}:{PORT}...")

    # 2. Attendre la connexion du client
    conn, addr = server.accept()
    print(f"Connected by {addr}")

    # 3. Envoyer la clé publique au client MAINTENANT que 'conn' existe
    conn.send(pickle.dumps(public_key))

    while True:
        try:
            data = conn.recv(4096)
            if not data:
                break
            
            # Réception du tuple (clé_AES_chiffrée, message_chiffré)
            encrypted_key, encrypted_message = pickle.loads(data)
            
            # Déchiffrement
            decrypted_message = decrypt_message(encrypted_key, encrypted_message, private_key)
            print(f"Client: {decrypted_message}")
            
        except Exception as e:
            print(f"Connection error: {e}")
            break

    print("Closing connection.")
    conn.close()
    server.close()

if __name__ == "__main__":
    main()
