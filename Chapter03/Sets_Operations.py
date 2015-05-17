#!/usr/bin/env python

set_a = set(range(0, 10, 2))
set_b = set(range(5, 10))
set_c = set(range(5, 15))

# String representation
print str(set_a)
print str(set_b)
print str(set_c)

# Number of members
print len(set_a)

# Membership test
print 6 in set_a

# Is disjoint
print set_b.isdisjoint(set_a)

# Is subset
print set_b <= set_c

# Is superset
print set_c >= set_b

# Union
print set_a | set_b

# Intersection
print set_a & set_b

# Difference
print set_a - set_b

# Symmetric Difference
print set_a ^ set_b
