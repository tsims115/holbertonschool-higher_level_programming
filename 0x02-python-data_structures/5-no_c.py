#!/usr/bin/python3
def no_c(my_string):
    idx = 0
    if my_string == "":
        return
    for c in my_string:
        if c == 'c' or c == 'C':
            my_string = my_string[:idx] + my_string[idx + 1:]
        idx += 1
    return my_string
