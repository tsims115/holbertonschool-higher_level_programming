#!/usr/bin/python3
"""Module models.square with Class square
    Inherits from rectangle"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square inherits from rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def update(self, *args, **kwargs):
        count = 0
        for i in args:
            if count == 0:
                self.id = i
            elif count == 1:
                self.size = i
            elif count == 2:
                self.x = i
            elif count == 3:
                self.y = i
            count += 1
        if args:
            return
        for k, v in kwargs.items():
            if hasattr(self, k):
                if k == "size":
                    self.integer_validator("width", v)
                else:
                    self.integer_validator(k, v)
                setattr(self, k, v)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.integer_validator("width", value)
        self.width = value
        self.height = value
