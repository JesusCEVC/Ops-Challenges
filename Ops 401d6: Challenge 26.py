#!/usr/bin/python3

import smtplib
import datetime
import time
import os
import logging
from getpass import getpass

# Set up logging
logging.basicConfig(filename='monitor.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Declare Vars
up = "Network is active"
down = "Network is down"
last = 0
ping_result = 0
email = input("Type your email here: ")
password = getpass("Type your password here: ")
ip = input("Type the IP you want to monitor here: ")

# Functions

# Function for sending an email when the server is up
def send_up_alert():
    now = datetime.datetime.now()
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(email, password)
    message = "Server is alive again"
    s.sendmail("scalio137@gmail.com", email, message)
    s.quit()
    logging.info("Server is alive again - Email sent")

# Function for sending an email when the server goes down
def send_down_alert():
    now = datetime.datetime.now()
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(email, password)
    message = "Server is down, RIP"
    s.sendmail("scalio137@gmail.com", email, message)
    s.quit()
    logging.warning("Server is down - Email sent")

# Function to perform a ping test
def ping_test():
    global last
    global ping_result

    if ping_result != last:
        if ping_result == up:
            send_up_alert()
        elif ping_result == down:
            send_down_alert()
        last = ping_result

    response = os.system("ping -c 1 " + ip)
    if response == 0:
        ping_result = up
    else:
        ping_result = down

    logging.info("Ping test completed - Result: " + ping_result)

# Main loop
while True:
    try:
        ping_test()
        time.sleep(2)
    except Exception as e:
        logging.error("An error occurred: " + str(e))
