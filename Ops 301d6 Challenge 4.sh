#!/bin/bash

# Set a backup directory
BACKUP_DIR="/var/log/backups"
mkdir -p $BACKUP_DIR

# Get current timestamp
TIMESTAMP=$(date "+%Y%m%d%H%M%S")

# Compression Action
SYSLOG_FILE="/var/log/syslog"
SYSLOG_SIZE=$(du -h $SYSLOG_FILE | awk '{print $1}')
SYSLOG_BACKUP="$BACKUP_DIR/syslog-$TIMESTAMP.zip"
zip -q $SYSLOG_BACKUP $SYSLOG_FILE
echo "$SYSLOG_FILE has been compressed into $SYSLOG_BACKUP"
echo "Before: $SYSLOG_SIZE"
echo "After: $(du -h $SYSLOG_BACKUP | awk '{print $1}')"

# Clear file
echo -n "" > $SYSLOG_FILE

# Compression Action
WTMP_FILE="/var/log/wtmp"
WTMP_SIZE=$(du -h $WTMP_FILE | awk '{print $1}')
WTMP_BACKUP="$BACKUP_DIR/wtmp-$TIMESTAMP.zip"
zip -q $WTMP_BACKUP $WTMP_FILE
echo "$WTMP_FILE has been compressed into $WTMP_BACKUP"
echo "Before: $WTMP_SIZE"
echo "After: $(du -h $WTMP_BACKUP | awk '{print $1}')"

# Clear file
echo -n "" > $WTMP_FILE

# Compare Sizes
echo "Lets check the difference:"
echo "  $SYSLOG_FILE: $SYSLOG_SIZE vs $(du -h $SYSLOG_BACKUP | awk '{print $1}')"
echo "  $WTMP_FILE: $WTMP_SIZE vs $(du -h $WTMP_BACKUP | awk '{print $1}')"


