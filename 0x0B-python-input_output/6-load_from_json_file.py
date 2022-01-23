#!/usr/bin/python3
"""Module 6-load_from_json_file with Function load_from_json_file"""


import json


def load_from_json_file(filename):
    """load_from_json_file - load an object from a json file
        filename: file to load from
        Return: object
    """
    with open(filename, 'r') as f:
        obj = json.load(f)
    return obj
