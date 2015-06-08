#!/usr/bin/env python

import numpy

# Do some arithmetic
angles_deg = numpy.array(range(0, 360, 15))
angles_rad = numpy.radians(angles_deg)
angles_sine = numpy.sin(angles_rad)

# Print the results
print "DEG\tRAD\t\tSINE"
for deg, rad, sine in zip(angles_deg, angles_rad, angles_sine):
    print "%d\t%f\t%f" % (deg, rad, sine)
