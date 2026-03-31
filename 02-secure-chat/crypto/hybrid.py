from crypto.rsa import generate_keys, encrypt as rsa_encrypt, decrypt as rsa_decrypt
from crypto.aes import generate_key, encrypt as aes_encrypt, decrypt as aes_decrypt


# Hybrid encryption
def encrypt_message(message, public_key):
    # Generate AES key
    aes_key = generate_key()

    # Encrypt message with AES
    encrypted_message = aes_encrypt(message, aes_key)

    # Encrypt AES key with RSA
    encrypted_key = rsa_encrypt(aes_key.decode('latin-1'), public_key)

    return encrypted_key, encrypted_message


# Hybrid decryption
def decrypt_message(encrypted_key, encrypted_message, private_key):
    # Decrypt AES key with RSA
    decrypted_key_str = rsa_decrypt(encrypted_key, private_key)
    aes_key = decrypted_key_str.encode('latin-1')

    # Decrypt message with AES
    decrypted_message = aes_decrypt(encrypted_message, aes_key)

    return decrypted_message


# Test
if __name__ == "__main__":
    public, private = generate_keys()

    message = "This is a top secret message"
    print("Original:", message)

    encrypted_key, encrypted_message = encrypt_message(message, public)

    print("Encrypted AES key:", encrypted_key)
    print("Encrypted message:", encrypted_message)

    decrypted = decrypt_message(encrypted_key, encrypted_message, private)

    print("Decrypted:", decrypted)
