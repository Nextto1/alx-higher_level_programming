#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Square representation
    Attributes:
        __size (int): size of the square side
    """
    def __init__(self, size=0):
        """The square initialises
        Args:
            size (int): size of the square side
        Returns:
            None
        """
        self.size = size

    def area(self):
        """The square's area calculation
        Returns:
            The  square area
        """
        return (self.__size) ** 2

    @property
    def size(self):
        """getter of __size
        Returns:
            The square side
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter of __size
        Args:
            value (int): size of the square side
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

    def my_print(self):
        """prints the square
        Returns:
            None
        """
        if self.__size == 0:
            print()
            return
        for e in range(self.__size):
            print("".join(["#" for j in range(self.__size)]))
