#!/usr/bin/python3
"""
This module supplies one function, say_my_name.
"""


def say_my_name(first_name, last_name=""):
    if type(first_name) is not str:
        raise TypeError("It must be a string")
    if type(last_name) is not str:
        raise TypeError("It must also be a string")
    print("My name is", first_name, last_name)
