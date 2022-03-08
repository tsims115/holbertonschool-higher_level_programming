#!/usr/bin/python3
"""Module 0-hbtn_status.py that fethces a url"""
import urllib.request

if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        html = response.read()
    print(html)
