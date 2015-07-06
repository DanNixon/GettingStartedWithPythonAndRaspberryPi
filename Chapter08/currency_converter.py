#!/usr/bin/env python

import urllib2
import json
from string import Template
import sys


URL_TEMLATE = Template('http://api.fixer.io/latest?base=${from_curr}&symbols=${to_curr}')
RESULT_TEMPLATE = Template('${symbol}\t\t${rate}\t${value}')


def get_rates(from_curr, to_currs):
    """
    Get the conversion rates for a set of currencies.

    @param from_curr The starting currency symbol
    @param to_currs List of symbols to get rates for
    @return Dictionary of symbols to rates
    """

    target_currencies = ','.join(to_currs)

    api_url = URL_TEMLATE.substitute(from_curr=from_curr,
                                     to_curr=target_currencies)

    response = urllib2.urlopen(api_url)

    json_response = response.read()
    result = json.loads(json_response)

    return result['rates']


def convert(from_value, from_curr, to_currs):
    """
    Converts a value in one currency to several others.

    @param from_value Value in starting currency
    @param from_curr The starting currency symbol
    @param to_currs List of symbols to convert to
    @return List of conversions
    """

    rates = get_rates(from_curr, to_currs)

    conversions = list()
    for symbol in to_currs:
        new_value = rates[symbol] * from_value
        conversion = {'symbol':symbol,
                      'rate': rates[symbol],
                      'value': new_value}
        conversions.append(conversion)

    return conversions


def process_cli(params):
    """
    Performs a conversion to several other currencies based on command line
    arguments.

    @param params Parameters from command line (excluding first index)
    """

    value_to_convert = float(params[0])
    start_currency = params[1].upper()
    conversion_currencies = [curr.upper() for curr in params[3:]]
    conversions = convert(value_to_convert,
                          start_currency,
                          conversion_currencies)

    print '%.2f %s in:' % (value_to_convert, start_currency)

    print 'CURRENCY\tRATE\t\tVALUE'
    for c in conversions:
        print '%s\t\t%.2f\t\t%.2f' % (c['symbol'], c['rate'], c['value'])


if __name__ == "__main__":
    process_cli(sys.argv[1:])
