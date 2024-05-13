#!/usr/bin/python3

"""
This Python script takes a URL and an email address as command-line arguments
sends a POST request to the specified URL with the email as a parameter
and then displays the body of the response
"""

import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    request = requests.post(url, data=value)
    print(request.text)
