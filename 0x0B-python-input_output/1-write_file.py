#!/usr/bin/python3
"""Module 1-write_file with function write_file"""


def write_file(filename="", text=""):
    """write_file - writes a string to a text file
        filename: file to write to
        text: string to write
        Return: number of characters written
    """
    with open(filename, 'w+') as f:
        data = f.read()
        f.seek(0)
        num_chars = f.write(text)
        f.truncate()
    return num_chars
