#!/usr/bin/python3
def text_indentation(text):
    flag = 0
    for c in text:
        if flag == 1:
            flag = 0
            if c == ' ':
                continue
        if c == '?' or c == '.' or c == ':':
            flag = 1
            print("{}".format(c))
            continue
        print("{}".format(c), end="")
