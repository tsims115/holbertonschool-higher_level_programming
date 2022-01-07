#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    list1 = [0, 0]
    lena = len(tuple_a)
    lenb = len(tuple_b)
    for i in range(2):
        if i + 1 <= lena:
            list1[i] += tuple_a[i]
        if i + 1 <= lenb:
            list1[i] += tuple_b[i]
    new_tup = (list1[0], list1[1])
    return new_tup
