#!/usr/bin/env python

import sys
from random import randint
from time import sleep
from picamera import PiCamera
import RPi.GPIO as GPIO

# Get input from command line
filename = sys.argv[1]
effect_type = sys.argv[2]

# Validate the command line options
if effect_type not in ['colour', 'filter', 'both']:
    print "Effect type must be one of: colour, filter, both"
    sys.exit(1)

# Default colour effect
colour = None
# Generate a random colour effect
if effect_type in ['colour', 'both']:
    colour = (randint(0, 256), randint(0, 256))
    print "Colour effect: " + str(colour)

# Default filter
image_effect = 'none'
# Generate a random filter
if effect_type in ['filter', 'both']:
    image_effect = PiCamera.IMAGE_EFFECTS.keys()[randint(0, len(PiCamera.IMAGE_EFFECTS))]
    print "Filter: " + image_effect

with PiCamera() as cam:
    cam.resolution = (1280, 720)
    cam.image_effect=image_effect
    cam.color_effects=colour
    cam.start_preview()
    sleep(15)
    cam.capture(filename)
