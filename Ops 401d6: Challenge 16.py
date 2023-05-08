import time

print("Select a mode:")
print("1. Offensive; Dictionary Iterator")
print("2. Defensive; Password Recognized")

mode = input("Enter mode number (1 or 2): ")

if mode == '1':
    word_list_file = input("Enter word list file path: ")
    with open(word_list_file, 'r') as f:
        for word in f:
            word = word.strip()
            print(word)
            time.sleep(0.5)
elif mode == '2':
    password = input("Enter password: ")
    word_list_file = input("Enter word list file path: ")
    with open(word_list_file, 'r') as f:
        word_list = [line.strip() for line in f]
        if password in word_list:
            print("Password recognized.")
        else:
            print("Password not recognized.")
else:
    print("Invalid mode selected.")
