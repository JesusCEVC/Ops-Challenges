#!/usr/bin/env python3

import os

# Head: define a func that lists requested items.
def list_all_files(directory_path):

    # Make a list to store items
    file_list = []
    
    # Use the os.walk() to move through dir
    for root, dirs, files in os.walk(directory_path):
        # Go over cd
        for name in files:
            # add path
            file_list.append(os.path.join(root, name))
        # Go over each dir
        for name in dirs:
            # Add dir
            file_list.append(os.path.join(root, name))
    
    return file_list

# Body: Read
if __name__ == "__main__":
    # Ask the user for a directory path
    directory_path = input("Enter a directory path: ")
    
    # Use the function
    file_list = list_all_files(directory_path)

    # End: Print the requested info
    for file_path in file_list:
        print(file_path)
