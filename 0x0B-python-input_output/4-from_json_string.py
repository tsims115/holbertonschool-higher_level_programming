#!/usr/bin/python3
"""Module def 4-from_json_string with function from_json_string"""


import json


def from_json_string(my_str):
    """from_json_string - returns an obj repr by a JSON string
        my_str: string to use
        Return: an object repre by JSON string
    """

    return json.loads(my_str)
