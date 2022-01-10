#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_set = set()
    if not set_1 or not set_2:
        return None
    for i in set_1:
        if i in set_2:
            continue
        else:
            new_set.add(i)
    for j in set_2: 
        if j in set_1:
            continue
        else:
            new_set.add(j)
    return new_set
