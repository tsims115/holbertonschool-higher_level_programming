#!/usr/bin/python3
""""""


Pizza = __import__("classTest").Pizza


class Calzone(Pizza):
    """Class Calzone"""
    num_calzones = 0

    def __init__(self, tops=[], diameter=0):
        super().__init__(tops, None, diameter)
        Pizza.num_pizzas -= 1
        Calzone.num_calzones += 1

    def __str__(self):
        return "{} inch calzone".format(self.diameter)

"""calzone = Calzone(["Pepperoni", "Mozzarella", "Ham"], 12)
print(calzone.diameter)
print(calzone.tops)
"""