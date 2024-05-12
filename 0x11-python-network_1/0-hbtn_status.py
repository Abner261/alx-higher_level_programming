#!usr/bin/python3
"""
This script sends a GET request to the provided URL
using 'urllib.request.urlopen()' and then reads
the response body using 'response.read()' Finally,
it prints the type, content, and utf-8 decoded content of the response body
"""
import urllib.request

url = "https://alx-intranet.hbtn.io/status"

with urllib.request.urlopen(url) as response:
    body = response.read()
    print("Body response:")
    print("\t- type:", type(body))
    print("\t- content:", body)
    print("\t- utf8 content:", body.decode('utf-8'))
