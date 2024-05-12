#!/usr/bin/python3

"""
This script takes a URL provided as a command-line argument and sends
a GET request to that URL using `urllib.request.urlopen()`
After receiving the response, it extracts the headers from the response
using `response.info()` and retrieves the value of the 'X-Request-Id' header
Finally, it prints the value of the 'X-Request-Id' header
"""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        header = response.info()
        print(header['X-Request-Id'])
