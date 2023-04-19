#!/usr/bin/python

# Import Libraries
import os
import time
from datetime import datetime

# Define the target and delay
target = "8.8.8.8"
interval = 2

# Define the function that handles the pinging
def check_ping(target):
    response = os.system("ping -c 1 " + target)

    # Check if the host is active or not with variables
    if response == 0:
        status = "Network Active"
    else:
        status = "Network Error"

    return status

# Ping the target IP every two seconds and print the status and when
while True:
    status = check_ping(target)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    print(f"{timestamp} {status} to {target}")
    time.sleep(interval)
