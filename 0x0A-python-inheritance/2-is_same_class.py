#!/usr/bin/python3
"""Module 2-is_same_class with function is_same_class"""


def is_same_class(obj, a_class):
    """Function is_same_class
        obj: object to check type
        a_class: class to check obj with
        Return: True if obj is an exact instance or False
    """
    return type(obj) is a_class
