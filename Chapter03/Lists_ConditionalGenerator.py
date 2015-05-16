#!/usr/bin/env python

# Options: french_toast, toast, cereal
breakfast = "french_toast"

def needed_for(meal, item):
    if meal == "french_toast":
        return item in ["bread", "eggs"]
    if meal == "toast":
        return item in ["bread"]
    if meal == "cereal":
        return item in ["milk", "cereal"]

all_items = ["apples", "onions", "cereal", "milk", "bread", "bacon", "eggs"]
l = [item for item in all_items if needed_for(breakfast, item)]

print str(l)
