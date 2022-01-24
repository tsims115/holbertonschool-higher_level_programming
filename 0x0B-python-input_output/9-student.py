#!/usr/bin/python3
"""Module 9-student with cladd Student"""


class Student:
    """Class Student
        public instance attributes:
            first_name, last_name, age
    """

    def __init__(self, first_name, last_name, age):
        """Instanciate public attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns dict representation of Student instance"""
        return self.__dict__
