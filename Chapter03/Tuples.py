#!/usr/bin/env python

t = ("Hello", 42, 42, "#")

# Iteration
for i in t:
    print i

# String representation
print str(t)

# Size
print len(t)

# Getter
print t[0]
print t[-2]

# Slicing
print t[2:4]

# Number of a given element
print t.count(42)

# Index of a given element
print t.index("#")
