#!/bin/bash

email=<EMAIL>
FILE=/usr/local/scripts/test.txt

#Check to see if a file can be created
touch $FILE

if [ -f $FILE ]
then
    rm $FILE
    echo "File System is good"
else
    echo "$HOSTNAME: File System Read-Only. System has been restarted" | mail -s "$HOSTNAME: R/O FileSystem" $email
    reboot -f
fi
