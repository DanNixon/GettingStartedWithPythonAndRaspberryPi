#!/usr/bin/env python

import RPi.GPIO as GPIO
from time import sleep

# Use GPIO numbering
GPIO.setmode(GPIO.BCM)

# List of putput GPIOs
led_gpios = [4, 17]

# Set up GPIOs setting every other output high (starting with the first)
for i, gpio in enumerate(led_gpios):
    state = i % 2 == 0
    GPIO.setup(gpio, GPIO.OUT, initial=state)

# Toggle the states of each output 10 times
for _ in range(10):
    # Get list of current states
    states = [not GPIO.input(gpio) for gpio in led_gpios]
    # Update outputs with new states
    GPIO.output(led_gpios, states)
    sleep(1.0)

# Reset GPIO configuration
GPIO.cleanup()
