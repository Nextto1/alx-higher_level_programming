#!/usr/bin/python3
"""
the is_kind_of_class  module
"""


def is_kind_of_class(obj, a_class):
    """True if object is an instance or inherited from a_class, else False"""
    return (isinstance(obj, a_class))
