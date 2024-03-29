#!/usr/bin/python3
"""
It defines a class Rectangle
"""


class Rectangle:
    """A rectangle representation"""
    def __init__(self, width=0, height=0):
        """Rectangle initialization"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """an intake of private instance attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """private instance attribute width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """an intake for a private instance attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """private instance attribute height setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
