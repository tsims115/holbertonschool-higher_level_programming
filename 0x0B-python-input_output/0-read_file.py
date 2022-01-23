#!/usr/bin/python3
"""Module 0-read_file.py"""


def read_file(filename=""):
    """Function read_file - prints to stdout content of file
        filename: name of file to read
    """
    with open(filename, 'r') as f:
        print(f.read(), end="")
