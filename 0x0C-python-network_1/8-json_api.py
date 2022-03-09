#!/usr/bin/python3
"""Module 8-json_api fethces https://intranet.hbtn.io/status"""


import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    if len(sys.argv) <= 2 or isdigit(sys.argv[2]):
        q = ""
    else:
        q = sys.argv[2]
    data = {
        'q': q
    }
    r = requests.post(url, data)
    try:
        if r.json() == {}:
            print("No result")
            return
        print("[{}] {}".format(r.json().get('id'), r.json().get('name')))
    except requests.exceptions.JSONDecodeError:
        print("Not a valid JSON")
