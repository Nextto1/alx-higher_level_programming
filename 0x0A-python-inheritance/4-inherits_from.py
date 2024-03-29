#!/usr/bin/python3
"""
That's the inherits_from function
"""


def inherits_from(obj, a_class):
    """It returns true if obj is a subclass of a_class, otherwise false"""
    return(issubclass(type(obj), a_class) and type(obj) != a_class)
