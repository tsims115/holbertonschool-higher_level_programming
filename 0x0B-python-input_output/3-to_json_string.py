#!/usr/bin/python3
"""Module 3-to_json_string with function to_json_string"""

import json


def to_json_string(my_obj):
    """to_json_string - returns a JSON repr of a string
        my_obj: object to repr as JSON
        Return: JSON repr of my_obj
    """

    return json.dumps(my_obj)
