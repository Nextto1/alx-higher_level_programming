#!/usr/bin/python3
"""
MyList class is located here
"""


class MyList(list):
    """the list subclass"""
    def __init__(self):
        """object initialization"""
        super().__init__()

    def print_sorted(self):
        """sorted list to be printed"""
        print(sorted(self))
