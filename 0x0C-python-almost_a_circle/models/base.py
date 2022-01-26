#!/usr/bin/python3
"""Module models.base with base class"""


import json


class Base:
    """Class Base that instanciates with id"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Instanciate with id if present"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Static method to get JSON string"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)
