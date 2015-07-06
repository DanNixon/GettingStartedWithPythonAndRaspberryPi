# -*- coding: utf-8 -*-

from datetime import datetime
import urllib2
from string import Template
import sys
from xml.dom.minidom import parse
import xml.dom.minidom


URL_TEMLATE = Template('http://api.openweathermap.org/data/2.5/forecast?q=${location}&mode=xml')

search_location = sys.argv[1]
api_url = URL_TEMLATE.substitute(location=search_location)

request = urllib2.Request(api_url)
response = urllib2.urlopen(request)
xml_response = response.read()

DOMTree = xml.dom.minidom.parseString(xml_response)
weather_data = DOMTree.documentElement

location = weather_data.getElementsByTagName('location')[0]
location_name = location.getElementsByTagName('name')[0].childNodes[0].data
location_country = location.getElementsByTagName('country')[0].childNodes[0].data

print '5 day forecast for %s, %s.\n' % (location_name, location_country)

forecasts = weather_data.getElementsByTagName('time')
for forecast in forecasts:
    api_time_string = forecast.getAttribute('from')
    time = datetime.strptime(api_time_string, '%Y-%m-%dT%H:%M:%S')
    time_string = datetime.strftime(time, '%H:%M %d %B')

    overview = forecast.getElementsByTagName('symbol')[0]
    overview_string = overview.getAttribute('name')

    temperature = forecast.getElementsByTagName('temperature')[0]
    temperature_string = '?'
    if temperature.hasAttribute('value'):
        # Convert from Kelvin to Celsius
        # (I'm sure the API is wrong when it claims the unit is already Celsius)
        temperature_string = '%.1f' % (float(temperature.getAttribute('value')) - 273.15)

    print u'%s: %s, %s°C' % (
            time_string,
            overview_string,
            temperature_string)
