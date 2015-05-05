#!/usr/bin/env bash

#SOURCE:
#http://www.linuxscrew.com/2009/04/02/tiny-bash-scripts-check-internet-connection-availability/

WGET=`which wget`

while true; do
$WGET -q --tries=10 --timeout=5 http://www.google.com -O /tmp/index.google &> /dev/null

    if [ ! -s /tmp/index.google ];then
        echo "No internet - power cycling!";
        sh powerCycle.sh;
    else
        echo "Internet OK. Going back to sleep.";
    fi
    sleep 10;
done
