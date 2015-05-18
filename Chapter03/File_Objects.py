#!/usr/bin/env python

import os.path

# The path to a file to write to
filename = os.path.expanduser("~/SampleFile.txt")

# Some text to write
text = "The quick, brown fox jumps, over the, lazy dog"

# Write some data to the file
with open(filename, "a") as f:
    lines = [l + "\n" for l in text.split(",")]
    f.writelines(lines)

# Read the data back from the file
with open(filename) as f:
    for idx, line in enumerate(f):
        # Print out the line number and the contents of the line
        print "%.2d: %s" % (idx, line.strip())

