#!/usr/bin/python3
"""
This is a module that creates a class
which returns a perimeter and the area of
rectangle
"""


class Rectangle:
    """
    This is a blueprint of a rectangle
    """

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width


    @property
    def height(self):
        return self.__height
    
    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("Width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        calculate area of a rectangle
        """

        return (self.__width) * (self.__height)

    def perimeter(self):
        """
        claculate perimeter of a rectangle
        """

        if self.__width == 0 and self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)
