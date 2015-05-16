#!/usr/bin/env python

values = range(0, 10, 2)
value_set = frozenset(values)

print str(value_set)

# This fails because frozenset is immutable
value_set.add(20)
