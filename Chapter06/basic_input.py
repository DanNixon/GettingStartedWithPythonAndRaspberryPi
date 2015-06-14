#!/usr/bin/env python

import RPi.GPIO as GPIO
from time import sleep

# Use GPIO numbering
GPIO.setmode(GPIO.BCM)

# GPIO with switch attached
switch_gpio = 17

# Set the GPIO up as an input will pullup resistor
GPIO.setup(switch_gpio, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while(True):
        # Read the status of the switch and print it
        state = not GPIO.input(switch_gpio)
        print "Switch is pressed: %d" % state
        sleep(1.0)

# Exit when Ctrl-C is pressed
except KeyboardInterrupt:
    # Reset GPIO configuration
    GPIO.cleanup()
