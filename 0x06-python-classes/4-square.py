#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """A square representation
    Attributes:
        __size (int): size of the square side
    """
    def __init__(self, size=0):
        """the square initialises
        Args:
            size (int): size of the square side
        Returns:
            None
        """
        self.size = size

    def area(self):
        """the square's area calculation
        Returns:
            The square area
        """
        return (self.__size) ** 2

    @property
    def size(self):
        """getter of __size
        Returns:
            The square size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter of __size
        Args:
            value (int): the size of the square size
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
