#!/usr/bin/python3
"""Module 8-rectangle with class Rectangle"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry
class Rectangle(BaseGeometry):
    """Class Rectangle inherits from BaseGeometry"""

    def __init__(self, width, height):
        if super().integer_validator("width", width):
            self.__width = width
        if super().integer_validator("height", height):
            self.__height = height

    def area(self):
        return self.__height * self.__width
