#!/bin/bash

# Take the date and time right now
date=$(date +"%m-%d-%Y_%H-%M-%S")

# Make the filename have the given date and time from above
LoggedEvent="syslog_$date"

# Copy /var/log/syslog to cd with the as above changed filename
cp /var/log/syslog "$LoggedEvent"
