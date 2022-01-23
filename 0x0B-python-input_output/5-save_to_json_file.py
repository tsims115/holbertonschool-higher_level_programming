#!/usr/bin/python3
"""Module save_to_json_file with function save_to_json_file"""


import json


def save_to_json_file(my_obj, filename):
    """save_to_json_file - writes an object to a text file
        my_obj: object to write
        filename: name of file to write to
    """

    with open(filename, 'w+') as f:
        json.dump(my_obj, f)
