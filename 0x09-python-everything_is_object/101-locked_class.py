#!/usr/bin/python3

"""This defines a locked class."""


class LockedClass:
    """
    It does away the user from instantiating new LockedClass attributes
    for anything but attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
