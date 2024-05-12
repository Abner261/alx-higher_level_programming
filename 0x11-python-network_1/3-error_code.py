#!/usr/bin/python3

"""
This script takes a URL as a command-line argument, sends a request to that URL
and displays the body of the response if the request is successfu
If the request encounters an HTTP error
it catches the error and prints the error code
"""
import sys
import urllib.error
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
