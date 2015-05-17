#!/usr/bin/env python

items = ["milk", "bread", "eggs", "cheese", "crackers"]
more_items = ["honey", "jam", "bread"]

# Iteration
for i in more_items:
    print i

# String representation
print str(items)

# Size
print len(items)

# Append items from another list
items.extend(more_items)
print items

# Getter
print items[2]

# Slicing
print items[1:3]
print items[::2]

# Existence  test
print "milk" in items

# Number of a given element
print items.count("bread")

# Insertion
items.append('tea')
print items

# Removal
items.remove("honey")
print items

# Sort
items.sort()
print items
