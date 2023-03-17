#!/bin/bash

while true; do
    # Print menu options
    echo "Please select an option:"
    echo "1. Hello world"
    echo "2. Ping self"
    echo "3. IP info"
    echo "4. Exit"
    
    # Get user input
    read -p "Enter your choice (1-4): " choice
    
    # Evaluate user input and take action
    if [ "$choice" -eq 1 ]; then
        echo "Hello world!"
    elif [ "$choice" -eq 2 ]; then
        ping -c 3 127.0.0.1 # ping loopback address
    elif [ "$choice" -eq 3 ]; then
        ifconfig # print network adapter information
    elif [ "$choice" -eq 4 ]; then
        exit 0 # exit program
    else
        echo "Apologies, that is not an option. Could you try a number between 1-4"
    fi
done
