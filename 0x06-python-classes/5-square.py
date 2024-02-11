#!/usr/bin/python3
"""Representing a square"""


class Square():
    """A square object representation"""

    def __init__(self, size=0):
        """ initialize the newly created square
        where: size equates the size of the square and given a default value 0
        """
        self.__size = size

        """Private attribute"""
    @property
    def size(self):
        """property getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """make the value of the set meet a standard"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """a public method that computes the area of the class obj"""
        return (self.__size * self.__size)

    def my_print(self):
        """Public instance method: that returns the current square area"""
        for item in range(self.__size):
            [print("#", end="") for j in range(self.__size)]
            print()
        if self.__size == 0:
            print()
