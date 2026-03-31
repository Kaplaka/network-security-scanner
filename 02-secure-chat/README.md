# End-to-End Encrypted Chat System (Hybrid Cryptography)

##  Project Overview
This project is a secure communication tool that demonstrates **End-to-End Encryption (E2EE)** using a hybrid cryptographic approach. It combines the security of **RSA** (Asymmetric) with the efficiency of **AES-style XOR** (Symmetric) encryption.

##  Accomplished Objectives
* **Hybrid Encryption Implementation**: Successfully integrated RSA and AES to secure both the data and the key exchange.
* **Socket Programming**: Developed a functional Client-Server architecture using Python's `socket` and `pickle` libraries.
* **Custom Crypto from Scratch**: Implemented core cryptographic logic without external high-level libraries to demonstrate deep understanding of the algorithms.

## How it Works
1. **The Handshake**: Upon connection, the Server sends its **RSA Public Key** to the Client.
2. **Key Encapsulation**: For every message, the Client generates a unique **AES key**, encrypts the message with it, and then encrypts the AES key using the Server's Public Key.
3. **Secure Decryption**: Only the holder of the **RSA Private Key** (the Server) can decrypt the AES key to unlock the message.

##  Technical Skills
* **Cryptography**: RSA, Symmetric/Asymmetric differences, Key exchange.
* **Network Security**: Secure socket handling, data serialization with `pickle`.
* **Python**: Modular code architecture and complex data structures.

---
**Author:** Jonas KAPLAKA(Student) – Cybersecurity Portfolio Project
