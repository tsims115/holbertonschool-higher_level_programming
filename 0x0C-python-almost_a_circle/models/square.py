#!/usr/bin/python3
"""Module models.square with Class square
    Inherits from rectangle"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square inherits from rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
