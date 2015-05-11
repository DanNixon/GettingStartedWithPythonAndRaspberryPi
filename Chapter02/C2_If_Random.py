#!/usr/bin/env python

import random

if random.randint(1, 100) % 2 == 1:
    print "Win!"
else:
    print "Lose!"
    
times_lost = 0
while random.randint(1, 100) % 2 == 0:
    times_lost += 1
print "Win! (after %d losses)" % (times_lost)
