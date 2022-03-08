#!/usr/bin/python3
"""Module 2-post_email.py sends a POST"""


import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        print("{}".format(response.read().decode('utf8')))
