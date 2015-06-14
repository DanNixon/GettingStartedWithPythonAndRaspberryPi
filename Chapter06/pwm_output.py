#!/usr/bin/env python

import RPi.GPIO as GPIO
from time import sleep


def do_fade(pwm, start, end, step=2):
    """
    Do a fade from a value to another.

    @param pwm PWM object
    @param start Staring value
    @param end Final value
    @param step Value change step
    """

    # Make step negative for a downwards fade
    # Modify the edn value accordingly as range is [start, end)
    if start > end:
        step *= -1
        end -= 1
    else:
        end += 1

    # Loop over the range of duty cycles
    for duty in range(start, end, step):
        pwm.ChangeDutyCycle(duty)
        sleep(0.1)


# Use GPIO numbering
GPIO.setmode(GPIO.BCM)

# GPIO with LED attached
led_gpio = 4

# Set up the GPIO as an output
GPIO.setup(led_gpio, GPIO.OUT)

# Setup the PWM driver at 50Hz
pwm = GPIO.PWM(led_gpio, 50)
pwm.start(0)

# Fade up then back down twice
for _ in range(2):
    do_fade(pwm, 0, 100)
    do_fade(pwm, 100, 0)

# Reset GPIO configuration
GPIO.cleanup()
