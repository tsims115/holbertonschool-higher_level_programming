#!/usr/bin/python3

class Pizza:
    num_pizzas = 0

    def __init__(self, tops=[], sauce="Classic Marinara", diameter=0):
        self.diameter = diameter
        self.tops = tops
        self.sauce = sauce
        Pizza.num_pizzas += 1

    @property
    def diameter(self):
        return self.__diameter

    @diameter.setter
    def diameter(self, value):
        self.__diameter = value

    def __str__(self):
        if self.diameter != 0:
            return "{} inch Pizza with {}".format(self.diameter, self.sauce)
        else:
            return "Need to set diameter of Pizza"

    """def __repr__(self):
        return self"""

    def __float__(self):
        return 10.52325

    def __int__(self):
        return 8
if __name__ == "__main__":
    print(Pizza.num_pizzas)
    pizza1 = Pizza(["Pepperoni", "Ham", "Mushroom"], "Cassic Marinara", 8)
    print(Pizza.num_pizzas)
    pizza2 = Pizza()
