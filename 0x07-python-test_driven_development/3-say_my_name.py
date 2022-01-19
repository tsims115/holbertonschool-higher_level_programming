#!/usr/bin/python3
"""Module 3-say_my_name includes function say_my_name"""


def say_my_name(first_name, last_name=""):
    """Function say_my_name prints first and last (if available)
        first_name: first name to print
        last_name: optional argument
        Return: nothing
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {}".format(first_name), end="")
    if last_name == "":
        print(" ")
    else:
        print(" {}".format(last_name))
