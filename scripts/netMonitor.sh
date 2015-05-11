#!/usr/bin/env bash

#SOURCE:
#http://www.linuxscrew.com/2009/04/02/tiny-bash-scripts-check-internet-connection-availability/

WGET=`which wget`

echo "Now monitoring your wireless network!";
/home/pi/wicycle/scripts/statusON.py &
sleep 90;

while true; do
$WGET -q --tries=10 --timeout=5 http://www.google.com -O /tmp/index.google &> /dev/null

    if [ ! -s /tmp/index.google ];then
        echo "No internet - power cycling!";
        /home/pi/wicycle/scripts/statusBlink_BAD.py &
        /home/pi/wicycle/scripts/powerCycle.py;
    else
        echo "Internet OK. Going back to sleep.";
        /home/pi/wicycle/scripts/statusBlink_OK.py &
    fi
    sleep 90;
done
