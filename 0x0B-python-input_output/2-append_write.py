#!/usr/bin/python3
"""Module 2-append_write.py with function append_write"""


from re import L


def append_write(filename="", text=""):
    """append_write - appends a string at the end of a text file
        filename: file to append to
        text: text to write
        Return: number of characters added
    """

    with open(filename, 'a+') as f:
        num = f.write(text)
    return num
