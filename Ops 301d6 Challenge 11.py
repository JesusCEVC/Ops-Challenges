#!/usr/bin/env python3

import requests

# Ask for a URL
url = input("Enter destination URL: ")

# Take your pick
print("Select an HTTP method:")
print("1. GET")
print("2. POST")
print("3. PUT")
print("4. DELETE")
print("5. HEAD")
print("6. PATCH")
print("7. OPTIONS")
http_method_choice = input("Enter your choice (1-7): ")

# Set Options
http_methods = ["GET", "POST", "PUT", "DELETE", "HEAD", "PATCH", "OPTIONS"]
http_method = http_methods[int(http_method_choice) - 1]

# Confirm Request and Yes/No
print(f"Sending {http_method} request to {url}")
confirmation = input("Confirm? (y/n): ")

if confirmation.lower() == "y":
    # Requests Library
    response = requests.request(http_method, url)

    # Status Codes
    status_code = response.status_code
    if status_code == 200:
        status_text = "OK"
    elif status_code == 201:
        status_text = "Created"
    elif status_code == 204:
        status_text = "No Content"
    elif status_code == 400:
        status_text = "Bad Request"
    elif status_code == 401:
        status_text = "Unauthorized"
    elif status_code == 403:
        status_text = "Forbidden"
    elif status_code == 404:
        status_text = "Site not found"
    elif status_code == 500:
        status_text = "Internal Server Error"
    else:
        status_text = "Unknown"
    print(f"Response status: {status_code} {status_text}")

    # Print Headers
    headers = response.headers
    print("Response headers:")
    for key, value in headers.items():
        print(f"{key}: {value}")
else:
    print("Request canceled.")
