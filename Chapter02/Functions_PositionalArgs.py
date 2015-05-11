#!/usr/bin/env python

def say_hello(*args):
    for person in args:
        print "Hello, %s!" % (person)

say_hello()
say_hello("Sanae")
say_hello("Remilia", "Yuuka", "Orin")
