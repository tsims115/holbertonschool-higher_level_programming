#!/usr/bin/python3
"""4-print_square module including print_square function"""


def print_square(size):
    """ print_square function - prints square based on size
        size: how big the square is and must be >= 0
        Return: nothing
    """

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
