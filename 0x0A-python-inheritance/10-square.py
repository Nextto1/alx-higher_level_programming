#!/usr/bin/python3
"""
The class BaseGeometry and subclass Rectangle
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A square representation"""
    def __init__(self, size):
        """instantiation of it"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """"the square area to be returned"""
        return self.__size ** 2
