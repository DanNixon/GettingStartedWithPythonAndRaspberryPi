#!/usr/bin/env python

import os.path

# Setup some sample files and paths
homedir = os.path.expanduser("~")
filename_in_homedir = os.path.expanduser("~/SampleFile.txt")
with open(filename_in_homedir, "w") as f:
    f.write("test\n")


# Get absolute path from a relative path
print os.path.abspath("SampleFile.txt")

# Get the basename (filename + exension) from a path
print os.path.basename(filename_in_homedir)

# Check if a file or directory exists
print os.path.exists(filename_in_homedir)

# Expand the user's home directpory
print os.path.expanduser("~/SampleFile.txt")

# Check if a path points to a file
print os.path.isfile(filename_in_homedir)

# Check if a path is a directory
print os.path.isdir(homedir)

# Check if a path is a symbolic link
print os.path.islink(homedir)

# Joins two paths
print os.path.join(homedir, "SampleFile.txt")

# Split the path from the filename
print os.path.split(filename_in_homedir)

# Split the path and filename from the extension
print os.path.splitext(filename_in_homedir)

# Get the size of a file or folder
print os.path.getsize(filename_in_homedir)

