#!/usr/bin/python3
"""Module models.rectangle with rectangle class"""


from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        """Instanciates width, height, x, y, and id
            first 4 attributes all have getter and setter methods
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def integer_validator(self, name, value):
        """Checks if value is an int
            name: name of value
            value: value to check if int
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if name == "x" or name == "y":
            if value < 0:
                raise ValueError("{} must be >= 0".format(name))
        elif value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def area(self):
        return self.height * self.width

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, value):
        self.integer_validator("width", value)
        self.__width = value

    @height.setter
    def height(self, value):
        self.integer_validator("height", value)
        self.__height = value

    @x.setter
    def x(self, value):
        self.integer_validator("x", value)
        self.__x = value

    @y.setter
    def y(self, value):
        self.integer_validator("y", value)
        self.__y = value
