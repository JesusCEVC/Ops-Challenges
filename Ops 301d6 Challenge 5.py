#!/usr/bin/env python3

# How to use Linux/Bash commands within Python
# First import the os library
import os

# Use os.popen() Taking the output of commands and stuffing them into some variables
whoami_output = os.popen("whoami").read()
lshw_output = os.popen("lshw -short").read()
ip_output = os.popen("ip a").read()

print("Output of 'ip a':")
print(ip_output)

print("Output of 'lshw -short':")
print(lshw_output)

print("Output of 'whoami':")
print(whoami_output)
