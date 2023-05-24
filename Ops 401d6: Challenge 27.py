#!/usr/bin/python3

import smtplib
import datetime
import time
import os
import logging
from getpass import getpass
from logging.handlers import RotatingFileHandler
from logging import StreamHandler

# Set up logging
log_file = 'monitor.log'
log_max_size = 1024  # Maximum log file size in kilobytes
log_backup_count = 3  # Number of backup log files to keep

# Create a rotating file handler for logging
file_handler = RotatingFileHandler(log_file, maxBytes=log_max_size * 1024, backupCount=log_backup_count)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

# Create a stream handler for logging to the terminal
stream_handler = StreamHandler()
stream_handler.setLevel(logging.INFO)
stream_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

# Create a logger and add the handlers
logger = logging.getLogger()
logger.addHandler(file_handler)
logger.addHandler(stream_handler)

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
    logger.info("Server is alive again - Email sent")

# Function for sending an email when the server goes down
def send_down_alert():
    now = datetime.datetime.now()
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(email, password)
    message = "Server is down, RIP"
    s.sendmail("AnonymousWorker157@gmail.com", email, message)
    s.quit()
    logger.warning("Server is down - Email sent")

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

    logger.info("Ping test completed - Result: " + ping_result)

# Main loop
while True:
    try:
        ping_test()
        time.sleep(2)
    except Exception as e:
        logger.error("An error occurred: " + str(e))
