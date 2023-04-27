#!/usr/bin/python3

from cryptography.fernet import Fernet
import os
import pyautogui

# Function to encrypt a file or directory recursively
def encrypt_path(path):
    if os.path.isfile(path):
        # Encrypt the file
        encrypt_file(path)
    elif os.path.isdir(path):
        # Encrypt all files and directories within the directory
        for filename in os.listdir(path):
            encrypt_path(os.path.join(path, filename))

# Function to decrypt a file or directory recursively
def decrypt_path(path):
    if os.path.isfile(path):
        # Decrypt the file
        decrypt_file(path)
    elif os.path.isdir(path):
        # Decrypt all files and directories within the directory
        for filename in os.listdir(path):
            decrypt_path(os.path.join(path, filename))

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
mode = input("Select a mode:\n1. Encrypt a file\n2. Decrypt a file\n3. Encrypt a message\n4. Decrypt a message\n5. Encrypt a directory\n6. Decrypt a directory\n")

# Handle the different modes
if mode == "1":
    # Prompt the user to provide a filepath to a target file
    file_path = input("Please provide the file path: ")
    encrypt_file(file_path)

elif mode == "

# set desktop wallpaper
SPI_SETDESKWALLPAPER = 20

# Set the path of the wallpaper image
wallpaper_path = "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.modernhoney.com%2Fchinese-orange-chicken%2F&psig=AOvVaw2tqgXeQq3Te1vPSfqZbdEU&ust=1682646307182000&source=images&cd=vfe&ved=0CBAQjRxqFwoTCODio434yP4CFQAAAAAdAAAAABAE"

# Download the wallpaper image and save it to a local file
os.system(f"curl {wallpaper_path} -o wallpaper.jpg")

# Set the wallpaper image as the desktop background
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, os.path.abspath("wallpaper.jpg"), 3)


# Define the message box parameters
message = "Hi friend! Accept this food"
title = "Popup Window"
style = 0x40 | 0x1  # MB_ICONINFORMATION | MB_OK

# Create the popup window
ctypes.windll.user32.MessageBoxW(None, message, title, style)


# Move the mouse to the center of the screen
pyautogui.moveTo(pyautogui.size().width / 2, pyautogui.size().height / 2)

# Click the left mouse button
pyautogui.click()

# Type a message
pyautogui.typewrite("Hello, World!")
