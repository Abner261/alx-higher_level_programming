#!/usr/bin/python3
"""
This script takes a URL and an email as command-line arguments
It encodes the email parameter, creates a POST request with the email parameter
sends the POST request to the provided URL,
and then prints the body of the response
"""

import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email})
    data = data.encode('utf-8')

    req = urllib.request.Request(url, data=data, method='POST')
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
