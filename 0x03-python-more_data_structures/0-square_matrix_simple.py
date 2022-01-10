#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [[]]
    for lis in matrix:
        list1 = []
        for i in lis:
            list1.append(i**2)
        if new_matrix == [[]]:
            new_matrix[0] = list1
        else:
            new_matrix.append(list1)
    return new_matrix
