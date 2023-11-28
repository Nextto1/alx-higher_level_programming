#!/usr/bin/python3
"""A scalar divide matrix function"""


def matrix_divided(matrix, div):
    """divides matrix by scalar integer and to two decimal places"""
    import decimal
    error_msg = "It must be a matrix of integers or floats"
    if type(matrix) is not list:
        raise TypeError(error_msg)
    len_rows = []
    row_count = 0
    for row in matrix:
        if type(row) is not list:
            raise TypeError(error_msg)
        len_rows.append(len(row))
        for element in row:
            if type(element) not in [int, float]:
                raise TypeError(error_msg)
        row_count += 1
    if len(set(len_rows)) > 1:
        raise TypeError("Each should have the same size")
    if type(div) not in [int, float]:
        raise TypeError("The number must be div")
    if int(div) == 0:
        raise ZeroDivisionError
    new_matrix = list(map(lambda row:
                          list(map(lambda x: round(x/div, 2), row)), matrix))
    return new_matrix
