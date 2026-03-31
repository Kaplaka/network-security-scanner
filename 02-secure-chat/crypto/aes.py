import os

# Generate random AES key
def generate_key(length=16):
    return os.urandom(length)

# XOR encryption (simple AES-style symmetric encryption)
def encrypt(message, key):
    message_bytes = message.encode()
    encrypted = bytes([message_bytes[i] ^ key[i % len(key)] for i in range(len(message_bytes))])
    return encrypted

# XOR decryption (same operation)
def decrypt(cipher, key):
    decrypted = bytes([cipher[i] ^ key[i % len(key)] for i in range(len(cipher))])
    return decrypted.decode()


# Test
if __name__ == "__main__":
    key = generate_key()

    message = "Hello AES Encryption"
    print("Original:", message)

    encrypted = encrypt(message, key)
    print("Encrypted:", encrypted)

    decrypted = decrypt(encrypted, key)
    print("Decrypted:", decrypted)
