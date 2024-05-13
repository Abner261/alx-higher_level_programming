#!/usr/bin/python3
"""
This script extracts the repository name and owner name from the
command-line arguments, constructs the GitHub API URL for fetching
commit information of the specified repository, sends a GET request
to this URL using the requests package, and prints out the SHA and
author's name of the last 10 commits if the request is successful
If the request fails, it prints an error message along
with the status code of the response
"""
import sys
import requests


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]

    url = 'https://api.github.com/repo/owner/commits'
    response = requests.get(url)
    json_resp = response.json()

    for commit in json_resp[:10]:
        commit_data = commit['commit']
        sha = commit_data.get('sha')
        author = commit_data.get('author').get('name')
        print(f"{sha}: {author}")
