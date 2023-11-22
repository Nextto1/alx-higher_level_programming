#!/usr/bin/python3
"""Square class definition"""


class Square:
    """A square represntation
    Attributes:
        __size (int):the size of the square side
    """
    def __init__(self, size):
        """A square initialises
        Args:
            size (int): the size of the square side
        Returns: None
        """
        self.__size = size
