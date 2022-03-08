#!/usr/bin/python3
"""Module 4-hbtn_status fethces https://intranet.hbtn.io/status"""


import sys
import requests


if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'
    r = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
