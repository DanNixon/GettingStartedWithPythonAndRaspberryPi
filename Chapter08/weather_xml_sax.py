# -*- coding: utf-8 -*-
#!/usr/bin/env python

from datetime import datetime
import urllib2
import xml.sax
from string import Template
import sys


class WeatherHandler(xml.sax.ContentHandler):

    def __init__(self):
        self._tag_buffer = list()

        self._location_name = '?'
        self._location_country = '?'

        self._time_string= ''
        self._overview_string = ''
        self._temperature_string = ''


    def startElement(self, tag, attributes):
        self._tag_buffer.append(tag)

        if self._tag_buffer[-2:] == ['weatherdata', 'location']:
            self._location_name = '?'
            self._location_country = '?'

        elif self._tag_buffer[-2:] == ['forecast', 'time']:
            time = datetime.strptime(attributes['from'], '%Y-%m-%dT%H:%M:%S')
            self._time_string = datetime.strftime(time, '%H:%M %d %B')

            self._overview_string = '?'
            self._temperature_string = '?'

        elif self._tag_buffer[-2:] == ['time', 'symbol']:
            if 'name' in attributes:
                self._overview_string = attributes['name']

        elif self._tag_buffer[-2:] == ['time', 'temperature']:
            if 'value' in attributes:
                self._temperature_string = '%.1f' % (float(attributes['value']) - 273.15)


    def endElement(self, tag):
        if self._tag_buffer[-2:] == ['weatherdata', 'location']:
            print '5 day forecast for %s, %s.\n' % (self._location_name, self._location_country)

        elif self._tag_buffer[-2:] == ['forecast', 'time']:
            print u'%s: %s, %s°C' % (
                    self._time_string,
                    self._overview_string,
                    self._temperature_string)

        self._tag_buffer.pop()


    def characters(self, content):
        if self._tag_buffer[-2:] == ['location', 'name']:
            self._location_name = content

        elif self._tag_buffer[-2:] == ['location', 'country']:
            self._location_country = content


URL_TEMLATE = Template('http://api.openweathermap.org/data/2.5/forecast?q=${location}&mode=xml')

search_location = sys.argv[1]
api_url = URL_TEMLATE.substitute(location=search_location)

response = urllib2.urlopen(api_url)
xml_response = response.read()

content_handler = WeatherHandler()

xml.sax.parseString(xml_response, content_handler)
