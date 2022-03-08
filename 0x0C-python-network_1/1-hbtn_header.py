#!/usr/bin/python3
"""Module 1-hbtn_header"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        print(response.__dict__['headers']['X-Request-Id'])
