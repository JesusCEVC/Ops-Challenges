#!/usr/bin/env python3

import requests
import webbrowser

targetsite = "http://www.whatarecookies.com/cookietest.asp"

# Send a GET request to the target site and store the response
response = requests.get(targetsite)

# Retrieve the cookies from the response
cookie = response.cookies

# Function to print the ASCII art of Cookie Monster
def bringforthcookiemonster():
    print('''
           .---. .---.
          :     : o   :    me want cookie!
      _..-:   o :     :-.._    /
  .-''  '  `---' `---' "   ``-.
.'   "   '  "  .    "  . '  "  `.
:   '.---.,,.,...,.,.,.,..---.  ' ;
`. " `.                     .' " .'
 `.  '`.                   .' ' .'
  `.    `-._           _.-' "  .'  .----.
    `. "    '"--...--"'  . ' .'  .'  o   `.

    ''')

# Function to send the cookie back to the site, capture the response, and open it in a browser
def send_cookie_back():
    # Set the 'Cookie' header with the retrieved cookie
    headers = {'Cookie': cookie}

    # Send a GET request to the target site with the cookie in the headers
    response = requests.get(targetsite, headers=headers)

    # Retrieve the HTML content from the response
    html_content = response.text

    # Write the HTML content to a file named 'response.html'
    with open('response.html', 'w') as file:
        file.write(html_content)

    # Open the generated HTML file in a new browser tab
    webbrowser.open('response.html', new=2)

# Call the function to print Cookie Monster ASCII art
bringforthcookiemonster()

# Print the target site URL
print("Target site is " + targetsite)

# Print the retrieved cookie
print(cookie)

# Call the function to send the cookie back and open the response in a browser
send_cookie_back()
