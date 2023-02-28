#!/bin/bash

# Script: Ops 201 Class 05 Ops Challenge Solution
# Author: Emilio Ceja
# Date of latest revision: 2-10-23
# Purpose: Write a script that displays running processes, asks the user for a PID, then kills the process with that PID.


# Main
while true
do
    echo "Select an option:"
    echo "1. Display Targets"
    echo "2. Eliminate Target"
    echo "3. Pack up and leave"
    read choice

    case $choice in
        1) 
            echo "Search Targets:"
            ps aux
            ;;
        2)
            echo "Enter your desired target (PID):"
            read pid
            kill $pid
            ;;
        3)
            echo "Getting out smoothly..."
            break
            ;;
        *) 
            echo "Target Missing"
            ;;
    esac
done




# End
