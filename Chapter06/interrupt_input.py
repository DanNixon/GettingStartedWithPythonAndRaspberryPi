#!/usr/bin/env python

import RPi.GPIO as GPIO
from time import sleep

# Use GPIO numbering
GPIO.setmode(GPIO.BCM)

# GPIO with LED attached
led_gpio = 4
# GPIO with switch attached
switch_gpio = 17

# Set the LED GPIO up as an output
GPIO.setup(led_gpio, GPIO.OUT)
# Set the switch GPIO up as an input will pullup resistor
GPIO.setup(switch_gpio, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def toggle_led(_):
    GPIO.output(led_gpio, not GPIO.input(led_gpio))


# Handle a switch press
GPIO.add_event_detect(switch_gpio, GPIO.FALLING, callback=toggle_led, bouncetime=500)

try:
    while(True):
        # Nothing to do in the main thread
        sleep(1.0)

# Exit when Ctrl-C is pressed
except KeyboardInterrupt:
    # Reset GPIO configuration
    GPIO.cleanup()
