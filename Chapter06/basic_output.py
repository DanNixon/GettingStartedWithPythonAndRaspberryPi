#!/usr/bin/env python

import RPi.GPIO as GPIO
from time import sleep

# Use GPIO numbering
GPIO.setmode(GPIO.BCM)

# GPIO with LED attached
led_gpio = 4

# Set the GPIO up as an output
GPIO.setup(led_gpio, GPIO.OUT)

# Toggle the state of the output 10 times
for _ in range(10):
    GPIO.output(led_gpio, not GPIO.input(led_gpio))
    sleep(1.0)

# Reset GPIO configuration
GPIO.cleanup()
