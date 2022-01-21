#!/usr/bin/python3
"""Module 1-my_list with class MyList"""


class MyList(list):
    """Class MyList public instance method
        inherits from list class with method print_sorted
    """

    def __init__(self):
        """initializes this object"""
        super().__init__()

    def print_sorted(self):
        """Prints list in sorted order (ascending)
        """

        print(sorted(self))
