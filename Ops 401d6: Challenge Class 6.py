#!/usr/bin/python3

from cryptography.fernet import Fernet
import os

# Function to encrypt a file
def encrypt_file(file_path):
    # Generate a new key
    key = Fernet.generate_key()

    # Load the file
    with open(file_path, 'rb') as f:
        file_data = f.read()

    # Encrypt the file data
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(file_data)

    # Write the encrypted data to the file
    with open(file_path, 'wb') as f:
        f.write(encrypted_data)

    # Write the key to a separate file
    with open(file_path + ".key", 'wb') as f:
        f.write(key)

    print(f"'{file_path}' has been encrypted.")


# Function to decrypt a file
def decrypt_file(file_path):
    # Load the key
    with open(file_path + ".key", 'rb') as f:
        key = f.read()

    # Load the encrypted data
    with open(file_path, 'rb') as f:
        encrypted_data = f.read()

    # Decrypt the data
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data)

    # Write the decrypted data to the file
    with open(file_path, 'wb') as f:
        f.write(decrypted_data)

    # Remove the key file
    os.remove(file_path + ".key")

    print(f"'{file_path}' has been decrypted.")


# Function to encrypt a message
def encrypt_message(cleartext):
    # Generate a new key
    key = Fernet.generate_key()

    # Encrypt the message
    fernet = Fernet(key)
    ciphertext = fernet.encrypt(cleartext.encode())

    # Print the ciphertext to the screen
    print("Ciphertext: ")
    print(ciphertext.decode())

    # Print the key to the screen
    print("Key: ")
    print(key.decode())


# Function to decrypt a message
def decrypt_message(ciphertext, key):
    # Decrypt the message
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(ciphertext.encode())

    # Print the decrypted message to the screen
    print("Decrypted message: ")
    print(decrypted_data.decode())


# Prompt the user to select a mode
mode = input("Select a mode:\n1. Encrypt a file\n2. Decrypt a file\n3. Encrypt a message\n4. Decrypt a message\n")

# Handle the different modes
if mode == "1":
    # Prompt the user to provide a filepath to a target file
    file_path = input("PLease Provide file path: ")
    encrypt_file(file_path)

elif mode == "2":
    # Prompt the user to provide a filepath to a target file
    file_path = input("Please provide the file path: ")
    decrypt_file(file_path)

elif mode == "3":
    # Prompt the user to provide a cleartext string
    cleartext = input("Provide the cleartext string: ")
    encrypt_message(cleartext)

elif mode == "4":
    # Prompt the user to provide a ciphertext and key
    ciphertext = input("Please provide ciphertext: ")
    key = input("Provide the key: ")
    decrypt_message(ciphertext, key)

else:
    print("Invalid mode selected.")
