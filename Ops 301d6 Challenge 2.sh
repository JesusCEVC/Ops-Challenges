#!/bin/bash

# Ask for a path to edit
echo "Enter the directory permissions should be changed for: "
read directory

# Request a perms number
echo "Please enter changes: "
read permissions

# Change the directory's perms
cd "$directory"
chmod -R "$permissions" *

# Display the changed settings
echo "Directory contents:"
ls -la "$directory"
