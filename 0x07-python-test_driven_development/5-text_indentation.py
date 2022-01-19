#!/usr/bin/python3
"""Module 5-text_indentation with text_indentation function"""


def text_indentation(text):
    """Function text_indentation
        text: text to print out and indent
    """

    flag = 0
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for c in text:
        if flag == 1:
            flag = 0
            if c == ' ':
                continue
        if c == '?' or c == '.' or c == ':':
            print("{}".format(c))
            print()
            flag = 1
            continue
        print("{}".format(c), end="")
    print()
