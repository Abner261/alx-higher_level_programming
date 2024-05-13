#!/usr/bin/python3

"""
This script extracts the URL from the command-line arguments
sends a GET request to the URL using the requests library
and retrieves the value of the 'X-Request-Id' variable from the response header
Finally, it prints the value of the 'X-Request-Id' variable
"""

import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    request_id = response.headers.get('X-Request-Id')

    print(request_id)
