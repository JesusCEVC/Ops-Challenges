#!/bin/bash

# Script: Ops 201 Class 04 Ops Challenge Solution
# Author: Emilio Ceja
# Date of latest revision:
# Purpose: Automation Script


# Main

# Create four game levels
mkdir Level1
mkdir Level2
mkdir Level3
mkdir BossLevel

directories=("Level1" "Level2" "Level3" "BossLevel")

for index in ${!directories[@]}
do
    filename="${directories[$index]}/file.txt"
    touch "$filename"
    echo "Loading..." > "$filename"
done

for index in ${!directories[@]}
do
    filename="${directories[$index]}/file.txt"
    if [ -f "$filename" ]
    then
        echo "Directory ${directories[$index]} has a file named file.txt."
    else
        echo "ERROR: Directory ${directories[$index]} does not have a file named file.txt."
    fi
done






# End
