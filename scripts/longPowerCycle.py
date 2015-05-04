#!/usr/bin/python

import RPi.GPIO as GPIO, time

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
time.sleep(10)
GPIO.cleanup()
