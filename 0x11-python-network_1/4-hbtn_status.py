#!/usr/bin/python3

"""
This script fetches the status of the Alx Intranet by sending a GET request
to the specified URL using the requests library. After receiving the response
it extracts the text content of the response. Then, it prints information about
the response body, including the type of the content and the content itself
"""

import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)
    content = response.text

    print("Body response:")
    print("\t- type:", type(content))
    print("\t- content:", content)
