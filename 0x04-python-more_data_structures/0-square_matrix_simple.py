#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square_value = []
    for line in matrix:
        square_value.append([k**2 for k in line])
    return square_value
