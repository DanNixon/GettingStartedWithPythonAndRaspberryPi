#!/usr/bin/env python

import sys
import serial

# Open the Raspberry Pi serial port
port = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=1)

# Write some data to the serial port
port.write('Hello, world!')

while True:
    # Get 1 byte of data from the serial port
    c = port.read()

    # Stop when we no longer get any data
    if len(c) == 0:
        break

    # Print the byte to the terminal
    sys.stdout.write(c)

# End the line
sys.stdout.write('\n')

# Close the serial port before exiting
port.close()
