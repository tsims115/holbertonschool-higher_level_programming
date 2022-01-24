#!/usr/bin/python3


Calzone = __import__("class2").Calzone
Pizza = __import__("classTest").Pizza

pizza1 = Pizza(["Pepperoni", "Ham", "Mushroom"], "Cassic Marinara", 8)
print(pizza1)
calzone1 = Calzone(["Pineapple", "Olives"], 10)
print(calzone1)
print(Pizza.num_pizzas)
print(Calzone.num_calzones)
print(repr(pizza1))
print(pizza1)
