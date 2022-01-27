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

    @classmethod
    def save_to_file(cls, list_objs):
        json_list = []
        if list_objs is not None:
            for obj in list_objs:
                json_dict = obj.to_dictionary()
                json_list.append(json_dict)
        json_string = Base.to_json_string(json_list)
        filename = cls.__name__ + ".json"
        with open(filename, 'w+') as f:
            data = f.read()
            f.seek(0)
            f.write(json_string)
            f.truncate()
