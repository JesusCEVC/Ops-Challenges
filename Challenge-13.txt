#!/bin/bash

# Function to retrieve information about a domain name
function get_domain_info {
    # Get domain from input
    read -p "Enter domain name: " domain

    # Run whois
    whois "$domain" > domain_info.txt

    # Run dig
    dig "$domain" >> domain_info.txt

    # Run host
    host "$domain" >> domain_info.txt

    # Run nslookup
    nslookup "$domain" >> domain_info.txt

    # Open in VSCode
    code domain_info.txt
}

# Menus
echo "What would you like to know?"
echo "1. Date and Time"
echo "2. Calendar"
echo "3. Directory"
echo "4. Contents"
echo "5. System Info"
echo "6. Domain name info"
read -p "Enter Desired Command: " choice

# Execute user choice
case $choice in
    1)
        date
        ;;
    2)
        cal
        ;;
    3)
        pwd
        ;;
    4)
        ls
        ;;
    5)
        uname -a
        ;;
    6)
        get_domain_info
        ;;
    *)
        echo "Invalid choice. Please try again."
        ;;
esac
# Backwards = closed
