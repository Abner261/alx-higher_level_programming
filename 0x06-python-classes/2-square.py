#!/usr/bin/python3
"""
This module shows one of the ways
used to validate the attribute size
"""


class Square:
    """
    Square class representation
    Attributes:
        __size (int): size of square
    """
    def __init__(self, size=0):
        """ acor """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
