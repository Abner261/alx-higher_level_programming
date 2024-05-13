#!/usr/bin/python3

"""
This script sends a GET request to the specified URL using the requests library
It then checks if the HTTP status code of the response is greater than or
equal to 400. If so, it prints an error message along with the HTTP status code
Otherwise, it prints the body of the response
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)
    if response.status_code >= 400:
        print("Error code:", response.status_code)
    else:
        print(response.text)
