#!/usr/bin/env python

dict_a = {"eggs": 1.50, "milk": 1.2, "bacon": 2.99}
dict_b = {"bread": 2.20, "jam": 4.87}
dict_c = {}

# String representation
print str(dict_a)
print str(dict_b)
print str(dict_c)

# Number of keys
print len(dict_a)

# Iteration
for key, value in dict_b.iteritems():
    print "%s -> %f" % (key, value)

# Set key
dict_c["honey"] = 5.32
print dict_c

# Get value
print dict_a["bacon"]

# Get value (safe)
print dict_b.get("bacon")

# Get calue (using default)
print dict_b.get("bacon", 6.0)

# Remove key
del dict_a["bacon"]
print dict_a

# Test for key
print "bacon" in dict_a

# Get list of items
print dict_a.items()

# Get list of keys
print dict_a.keys()

# Get list of items
print dict_a.values()

# Update dictionary from another
dict_c.update(dict_b)
print dict_c
