#!/usr/bin/python3
def common_elements(set_1, set_2):
    new_set = set()
    for e in set_1:
        if e in set_2:
            new_set.add(e)
    return new_set
