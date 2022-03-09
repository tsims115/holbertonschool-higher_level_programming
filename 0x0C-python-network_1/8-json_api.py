#!/usr/bin/python3
"""Module 8-json_api fethces https://intranet.hbtn.io/status"""


import requests
import sys


if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) <= 1 or isdigit(sys.argv[1]):
        q = ""
    else:
        q = sys.argv[1]
    data = {
        'q': q
    }
    r = requests.post(url, data)
    try:
        if r.json() == {}:
            print("No result")
        else:
            print("[{}] {}".format(r.json().get('id'), r.json().get('name')))
    except requests.exceptions.JSONDecodeError:
        print("Not a valid JSON")
