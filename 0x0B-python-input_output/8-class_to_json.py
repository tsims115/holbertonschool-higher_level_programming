#!/usr/bin/python3
"""Module 8-class_to_json with function class_to_json"""


import json


def class_to_json(obj):
    """class_to_json - returns dict description
        obj: class instance to get dict description of
    """
    return json.dumps(str(obj))
