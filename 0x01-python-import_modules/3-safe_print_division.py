#!/usr/bin/python3
def safe_print_division(a, b):
    if b == 0:
        b = None
    else:
        b = a / b
    print("Inside result: {}".format(b))
    return b

