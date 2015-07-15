#!/usr/bin/env python

from enum import Enum

# Create an enumeration type
class OperatingSystem(Enum):
    Windows = 1
    OSX = 2
    Linux = 3

# Show some details
print OperatingSystem
print dir(OperatingSystem)
print OperatingSystem.Linux
print OperatingSystem.Linux.value

