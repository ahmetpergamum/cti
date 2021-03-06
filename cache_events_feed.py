#!/usr/bin/env python
# -*- coding: utf-8 -*-

from keys import misp_url, misp_key
import argparse
from pymisp import PyMISP

# disable warning
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# For python2 & 3 compat, a bit dirty, but it seems to be the least bad one
try:
    input = raw_input
except NameError:
    pass
    
def init(url, key):
    return PyMISP(url, key, False, 'json', debug=False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Cache all events from a feed.')
    parser.add_argument("-f", "--feed", required=True, help="feed's ID to be cached.")
    args = parser.parse_args()
    
    misp = init(misp_url, misp_key)
    misp.cache_feed(args.feed)
