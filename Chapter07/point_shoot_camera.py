#!/usr/bin/env python

import sys
import os
from datetime import datetime
from string import Template
from time import sleep, time
from picamera import PiCamera
import RPi.GPIO as GPIO


# Create the directory in which captures will be saved
save_directory = sys.argv[1]

if not os.path.exists(save_directory):
    os.makedirs(save_directory)

capture_sw_gpio = 4
capture_mode_gpio = 17


def capture_still(filename, resolution=None):
    """
    Capture still image when capture button is released.
    @param filename Filename to save as
    @param resolution Resolution to capture at
    """
    print "Still mode"
    with PiCamera() as cam:
        cam.resolution = resolution if resolution is not None else (1280, 720)
        cam.start_preview()
        while not GPIO.input(capture_sw_gpio):
            sleep(0.5)
        cam.capture(filename)


def capture_video(filename, resolution=None):
    """
    Capture a video until capture button is released.
    @param filename Filename to save as
    @param resolution Resolution to capture at
    """
    print "Video mode"
    with PiCamera() as cam:
        cam.resolution = resolution if resolution is not None else (640, 480)
        cam.start_recording(filename)
        while not GPIO.input(capture_sw_gpio):
            cam.wait_recording(0.5)
        cam.stop_recording()


def handle_capture_start(_):
    """
    Handle the capture button being pressed.
    """
    print "Starting capture"

    # Determine capture mode
    mode_sw = GPIO.input(capture_mode_gpio)
    mode = 'still' if mode_sw else 'video'

    # Generate filename
    ext = 'jpg' if mode_sw else 'h264'
    timestamp = datetime.fromtimestamp(time()).strftime('%Y%m%d_%H%M%S')
    filename = Template("${datetime}_${mode}.${ext}").substitute(mode=mode, ext=ext, datetime=timestamp)
    filepath = os.path.join(save_directory, filename)

    # Call capture function
    if mode == 'still':
        capture_still(filepath)
    elif mode == 'video':
        capture_video(filepath)
    print "Capture saved to: " + filepath

# Setup GPIO
GPIO.setmode(GPIO.BCM)
# Both switches are active low, pull up pins
GPIO.setup(capture_sw_gpio, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(capture_mode_gpio, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# Add an event handler for the capture button being pressed
GPIO.add_event_detect(capture_sw_gpio, GPIO.FALLING, callback=handle_capture_start, bouncetime=500)

try:
    # Nothing to do on main thread
    while True:
        sleep(1)
except KeyboardInterrupt:
    # Clean up GPIO when exiting
    GPIO.cleanup()
