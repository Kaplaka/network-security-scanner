# Secure Chat - Hybrid Encryption (RSA + AES)

A secure client-server chat application using hybrid encryption:
- RSA for secure key exchange
- AES for message encryption
- TCP sockets for communication
- End-to-end encrypted messaging

## Features

- Secure client-server communication
- Hybrid encryption (RSA + AES)
- Bidirectional encrypted chat
- Username support
- Timestamped messages
- Python socket programming
- Cryptography implementation

## How It Works

1. Server generates RSA keys
2. Client connects and exchanges public keys
3. Client encrypts message using AES
4. AES key encrypted using RSA
5. Server decrypts RSA → gets AES key
6. Server decrypts message
7. Same process in reverse

## 📁 Project Structure

02-secure-chat/
│
├── __init__.py
├── client.py
├── server.py
├── README.md
│
└── crypto/
   ├── rsa.py
   ├── aes.py
   └── hybrid.py

## ▶️ Run

### Start server
python3 server.py
### Start client
python3 server.py

## Example
[14:42] Jonas: Hello
[14:42] Server: Secure channel established


## 🔐 Security Concepts

- Asymmetric encryption (RSA)
- Symmetric encryption (AES)
- Hybrid cryptosystem
- Secure key exchange
- End-to-end encryption
- Socket networking

## Educational Purpose

This project demonstrates how secure messaging systems like WhatsApp
and Signal implement hybrid encryption.

## Author

Cybersecurity Student – Secure Chat Project
