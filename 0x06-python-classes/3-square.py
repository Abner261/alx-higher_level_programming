#!/usr/bin/python3
"""
In this module we are focusing on introducing
another instance method that will be used to
calculate the area of a square
"""


class Square:
    """
    Square class representation
    Attributes:
        __size (int): size of square
    """
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ The area of a square """
        return self.__size ** 2
