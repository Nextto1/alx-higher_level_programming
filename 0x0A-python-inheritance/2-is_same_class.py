#!/usr/bin/python3
"""
The is_same_class module
"""


def is_same_class(obj, a_class):
    """It returns true if object is the exact class a_class, otherwise false"""
    return (type(obj) == a_class)
