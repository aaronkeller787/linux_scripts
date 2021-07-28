#!/bin/bash
UPMYSQL=$(pgrep mysql | wc -l);
UPHTTPD=$(pgrep httpd | wc -l);

email=<EMAIL ADDRESS HERE>

if [ "$UPMYSQL" -eq 0 ];
then
        echo "MySQL is down.";
        sudo service mysql start
        mount -a
        echo "$HOSTNAME: MySQL was not running and has been restarted." | mail -s "$HOSTNAME: MySQL Service Check" $email
else
        echo "MySQL is running.";
        echo "$HOSTNAME: MySQL is running. No action necessary at this time. " | mail -s "$HOSTNAME: MySQL Service Check " $email
fi

if [ "$UPHTTPD" -eq 0 ]
then
        echo "HTTPD is down"
        sudo service httpd start
        echo "$HOSTNAME: Httpd was not running and has been restarted." | mail -s "$HOSTNAME: Httpd Service Check" $email
else
        echo "HTTPD is running"
        echo "$HOSTNAME: HTTPD is running. No action necessary at this time" | mail -s "$HOSTNAME: Httpd Service Check" $email
fi
