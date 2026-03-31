import random
from math import gcd

def generate_keys():
    # Liste simplifiée pour le test (vous pourrez utiliser Miller-Rabin plus tard)
    primes = [101, 103, 107, 109, 113, 127, 131, 137, 139, 149]
    p = random.choice(primes)
    q = random.choice([x for x in primes if x != p])
    
    n = p * q
    phi = (p - 1) * (q - 1)
    
    e = 65537 # Exposant standard
    if gcd(e, phi) != 1:
        e = 3
        while gcd(e, phi) != 1:
            e += 2
            
    # Calcul de d (inverse modulaire)
    d = pow(e, -1, phi)
    
    return ((e, n), (d, n))

def encrypt(message, public_key):
    e, n = public_key
    # Convertit chaque caractère en nombre, chiffre, puis stocke en liste
    return [pow(ord(char), e, n) for char in message]

def decrypt(ciphertext, private_key):
    d, n = private_key
    # Déchiffre chaque nombre et reconstruit la chaîne
    return "".join([chr(pow(char, d, n)) for char in ciphertext])
# Test
if __name__ == "__main__":
    public, private = generate_keys()

    message = "Hello Secure World"
    print("Original:", message)

    encrypted = encrypt(message, public)
    print("Encrypted:", encrypted)

    decrypted = decrypt(encrypted, private)
    print("Decrypted:", decrypted)
