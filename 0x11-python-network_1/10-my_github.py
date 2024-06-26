#!/usr/bin/python3

"""
This script uses provided GitHub username and personal access token
to authenticate via Basic Authentication. It sends a GET request to the
GitHub API endpoint for user information. If successful (status code 200)
it prints the user id from the JSON response. Otherwise
it prints None to indicate an error
"""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    url = "https://api.github.com/user"

    response = requests.get(url, auth=(username, password))

    if response.status_code == 200:
        print(response.json()["id"])
    else:
        print(None)
