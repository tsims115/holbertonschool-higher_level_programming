#!/usr/bin/python3
"""Module 2-post_email.py sends a POST"""


import sys
import urllib.request
import urllib.parse
import urllib.error


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            print("{}".format(response.read().decode('utf8')))
    except urllib.error.URLError as e:
        print(e.reason)
