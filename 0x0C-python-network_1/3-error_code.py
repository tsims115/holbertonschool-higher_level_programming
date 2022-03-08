#!/usr/bin/python3
"""Module 3-post_email error code"""


import sys
from urllib import request, parse, error


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        req = request.Request(url)
        with request.urlopen(url) as response:
            print("{}".format(response.read().decode('utf8')))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
