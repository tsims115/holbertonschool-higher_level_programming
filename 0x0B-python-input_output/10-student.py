#!/usr/bin/python3
"""Module 10-student with Class Student"""


class Student:
    """Class Student
        public instance attributes:
            first_name, last_name, age
        public method to_json
    """

    def __init__(self, first_name, last_name, age):
        """Instanciate with given parameters"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """to_json public method"""
        if attrs is None:
            return self.__dict__
        if all(isinstance(s, str) for s in attrs):
            new_dict = {}
            for i in attrs:
                if i in self.__dict__:
                    new_dict[i] = self.__dict__[i]
            return new_dict
        else:
            return self.__dict__
