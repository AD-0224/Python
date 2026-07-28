import base64
import hashlib
import os

from cryptography.fernet import Fernet

def generate_salt():
    return os.urandom(16)

def save_salt(salt):
    with open("salt.bin", "wb") as file:
        file.write(salt)

def load_salt():
    with open("salt.bin", "rb") as file:
        return file.read()

def derive_key(password, salt):
# Generate a secure encryption key from the master password using PBKDF2
    key = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode(),
        salt,
        100000
    )
    return base64.urlsafe_b64encode(key)

def encrypt_password(password, key):
    fernet = Fernet(key)

    encrypted = fernet.encrypt(password.encode())
    return encrypted

def decrypt_password(encrypted_password, key):
    fernet = Fernet(key)

    decrypted = fernet.decrypt(encrypted_password)
    return decrypted.decode()
