#!/usr/bin/python

import RPi.GPIO as GPIO, time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(6, GPIO.OUT)

GPIO.output(6, GPIO.HIGH)
time.sleep(90)

GPIO.output(6, GPIO.LOW)
GPIO.cleanup()
