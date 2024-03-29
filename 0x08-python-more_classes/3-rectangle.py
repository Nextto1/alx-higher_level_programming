#!/usr/bin/python3
"""
It defines a class Rectangle
"""


class Rectangle:
    """A rectangle representation"""
    def __init__(self, width=0, height=0):
        """rectangle initialization"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """intake for private instance attribute width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """intake for private instance attribute width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """private instance attribute height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """private instance attribute height setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """rectangle area return"""
        return self.__width * self.__height

    def perimeter(self):
        """rectangle perimeter return"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """returns printable the rectangle string representation"""
        string = ""
        if self.__width != 0 and self.__height != 0:
            string += "\n".join("#" * self.__width
                                for j in range(self.__height))
        return string
