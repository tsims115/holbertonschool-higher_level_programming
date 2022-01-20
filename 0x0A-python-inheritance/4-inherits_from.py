#!/usr/bin/python3
"""Module 4-inherits_from with function inherits_from
"""


def inherits_from(obj, a_class):
    return issubclass(type(obj), a_class) and type(obj) is not a_class
