#!/usr/bin/env python

import random

number = random.randint(0, 3)
if number == 2:
    print "Big Win!"
elif number == 1:
    print "Small Win!"
else:
    print "Lose!"
