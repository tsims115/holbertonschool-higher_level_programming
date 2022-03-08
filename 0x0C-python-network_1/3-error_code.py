#!/usr/bin/python3
"""Module 3-post_email error code"""


import sys
from urllib import request, parse, error


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            print("{}".format(response.read().decode('utf8')))
    except urllib.error.URLError as e:
        print("Error code: {}".format(e.reason))
