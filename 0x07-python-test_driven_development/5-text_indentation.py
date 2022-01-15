#!/usr/bin/python3
def text_indentation(text):
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
            flag = 1
            continue
        print("{}".format(c), end="")
    print()
