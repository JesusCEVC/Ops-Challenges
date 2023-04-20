#!/usr/bin/python3

# Import Libraries
import smtplib
import datetime, time, os
from getpass import getpass

# Declare Vars
up = "Network is active"
down = "Network is down"
last = 0
ping_result = 0
email = input("Type your email here:")
password = getpass("Type your password here:")
ip = input("Type the IP you want to monitor here:")

# Functions

# function for when its up
def send_upAlert():
    now = datetime.datetime.now()
    s = smtplib.SMTP('smtp.gmail.com' , 587)
    s.starttls()
    s.login(password)
    message = "Server is living again"
    s.sendmail("scalio137@gmail.com", email, message)
    s.quit()

# Function for when it goes down
def send_downAlert():
    now = datetime.datetime.now()
    s = smtplib.SMTP('smtp.gmail.com' , 587)
    s.starttls()
    s.login(password)
    message = "Server is down, RIP"
    s.sendmail("scalio137@gmail.com", email, message)
    s.quit()

# Function to ping
def ping_test():

    if((ping_result != last) and (ping_result == up)):
        last = up
        send_upAlert
    elif ((ping_result != last) and (ping_result == down)):
        send_downAlert()
        last = down

    response = os.system("ping -c +1 " + ip)
    if response == 0:
        ping_result = up
    else:
        ping_result = down

# Infinite Loop
while True:
    ping_test()
    time.sleep(2)


