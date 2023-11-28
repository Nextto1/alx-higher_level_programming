#!/usr/bin/python3
"""
This module supplies one function, print_square(size).
"""


def print_square(size):
    if type(size) is not int:
        raise TypeError("It must be an integer")
    if size < 0:
        raise ValueError("It's size must be >= 0")
    if size > 0:
        print(("#" * size + "\n") * size, end="")
