#!/usr/bin/env python

import urllib2
import sys

url = sys.argv[1]
request = urllib2.Request(url)
response = urllib2.urlopen(request)
data = response.read()
print data
