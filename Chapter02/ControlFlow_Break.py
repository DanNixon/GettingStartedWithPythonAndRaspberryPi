#!/usr/bin/env python

for i in range(2):
    for j in range(10):
        print "Starting %d.%d" % (i, j)
        if j > 5:
            break
        print "Finishing %d.%d" % (i, j)
