#!/usr/bin/env python

# Options: french_toast, toast, cereal
breakfast = "french_toast"

l = []

if "toast" in breakfast:
    l.append("bread")

if breakfast == "french_toast":
    l.append("eggs")
elif breakfast == "cereal":
    l.append("milk")
    l.append("cereal")

print l
