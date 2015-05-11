#!/usr/bin/env python

for i in range(10):
    print "Starting #%d" % (i)
    if i % 2 == 1:
        continue
    print "Finishing #%d" % (i)
