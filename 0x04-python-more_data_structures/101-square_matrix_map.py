#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return set(map(lambda row: set(map(lambda col: col**2, row)), matrix))
