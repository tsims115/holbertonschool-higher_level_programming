#!/usr/bin/python3
"""Module 8-rectangle with class Rectangle"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Class Rectangle inherits from BaseGeometry"""

    def __init__(self, width, height):
        """initializes with width and height"""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """returns area with height and width"""
        return self.__height * self.__width

    def __str__(self):
        """string representation of object"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
