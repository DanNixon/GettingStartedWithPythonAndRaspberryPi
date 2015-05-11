#!/usr/bin/env python

def say_hello(*args, **kwargs):
    for person in args:
        greeting = kwargs.get("greeting", "Hello")
        print "%s, %s!" % (greeting, person)

say_hello()
say_hello("Tenshi")
say_hello("Eirin", "Keine", greeting="Good morning")
