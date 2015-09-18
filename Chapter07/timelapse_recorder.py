#!/usr/bin/env python

import sys
import os
from string import Template
from time import sleep
from threading import Thread
from picamera import PiCamera


class ImageCapture(Thread):
    """
    Thread usd to capture an image from the camera.
    """

    def __init__(self, filename, resolution=None, delay=1.0):
        Thread.__init__(self)
        self._filename = filename
        self._delay = delay
        self._resolution = resolution if resolution is not None else (1024, 768)

    def run(self):
        with PiCamera() as cam:
            cam.resolution = self._resolution
            cam.start_preview()
            sleep(self._delay)
            cam.capture(self._filename)


# Get input from command line
delay = float(sys.argv[1])
save_directory = sys.argv[2]

# Create the directory in which captures are saved
if not os.path.exists(save_directory):
    os.makedirs(save_directory)

# The format for image filenames
filename_format = Template("${frameno}_img.jpg")

# Loop to capture images until Ctrl-C
frame_no = 0
while True:
    filename = os.path.join(save_directory, filename_format.substitute(frameno=frame_no))
    ImageCapture(filename).start()
    frame_no += 1
    sleep(delay)
