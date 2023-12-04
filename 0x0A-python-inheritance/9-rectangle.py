#!/usr/bin/python3
"""
A class BaseGeometry and subclass Rectangle
"""


class BaseGeometry:
    """It contains public instance methods area and integer_validator"""
    def area(self):
        """when called it shows an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """A rectangle representation"""
    def __init__(self, width, height):
        """instantiation of it"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """the rectangle to be returned"""
        return self.__width * self.__height

    def __str__(self):
        """the rectangle string representation informally"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
