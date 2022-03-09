#!/usr/bin/python3
"""Module 4-hbtn_status fethces https://intranet.hbtn.io/status"""


import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = {
        'email': email
    }
    r = requests.post(url, data)
    print(r.text)
