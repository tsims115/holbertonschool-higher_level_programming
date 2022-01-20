#!/usr/bin/python3
"""Module 10-square with class Square"""


Rectangle = __import__("9-rectangle").Rectangle
class Square(Rectangle):
    """Class Square inherits from Rectangle"""
    def __init__(self, size):
        if super().integer_validator("size", size):
            super().__init__(size, size)
