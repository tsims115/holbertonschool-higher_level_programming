#!/usr/bin/python3
"""Module 5-base_geometry with class BaseGeometry"""


class BaseGeometry:
    """Class BaseGeometry with public method
    area(): raises an exception saying area is not implemented
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be >= 0".format(name))
