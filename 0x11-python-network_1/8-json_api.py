#!/usr/bin/python3

"""
This script checks if a letter is provided as a command-line argument
If not, it sets the value of the variable `q` to an empty string. Then
it sends a POST request to the specified URL with the letter as a parameter
After receiving the response, it attempts to parse it as JSON. If successful,
it prints the user ID and name from the response. If the response is not valid
JSON,it prints an error message. If the response is empty,it prints "No result"
"""

import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]

    url = "http://0.0.0.0:5000/search_user"
    payload = {"q": q}

    response = requests.post(url, data=payload)

    try:
        data = response.json()
        if data:
            print("[{}] {}".format(data['id'], data['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
