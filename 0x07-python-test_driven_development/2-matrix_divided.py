#!/usr/bin/python3
"""2-matrix_divided module
    includes error and matrix_divided functions
"""


def error(o):
    """error function - takes in one arg to determine what to raise
        o: error to raise
    """
    if o == 0:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
            )
    elif o == 1:
        raise TypeError(
            "Each row of the matrix must have the same size"
        )
    elif o == 2:
        raise TypeError(
            "div must be a number"
        )
    elif o == 3:
        raise ZeroDivisionError(
            "division by zero"
        )


def matrix_divided(matrix, div):
    """matrix_divide - divides matrix and returns new one
        matrix: matrix to divide
        div: what to divide matrix by
        Return: return a new matrix that is divided by div
    """
    new_matrix = []
    len1 = len(matrix[0])
    if not isinstance(div, int) and not isinstance(div, float):
        error(2)
    elif div == 0:
        error(3)
    for i in matrix:
        list1 = []
        for j in i:
            if not len1 == len(i):
                error(1)
            if not isinstance(j, int) and not isinstance(j, float):
                error(0)
            list1.append(round(j / div, 2))
        new_matrix.append(list1)
    return new_matrix
