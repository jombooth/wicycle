#!/usr/bin/python

import RPi.GPIO as GPIO, time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(6, GPIO.OUT)

counter = 60

while(counter > 0):
        counter -= 1
	GPIO.output(6, GPIO.LOW)
	time.sleep(.125)
	GPIO.output(6, GPIO.HIGH)
	time.sleep(.125)

GPIO.output(6, GPIO.LOW)
GPIO.cleanup()
