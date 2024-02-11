#!/usr/bin/python3

"""A MagicClass object created and it uses a math function
so a import math is been used
"""
import math


class MagicClass:
    """Represent a circle"""
    def __init__(self, radius=0):
        """initialize the magic class with the radius as a parameter"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """compute the area of the circle"""

        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """compute the circumference of a circle"""
        return (2 * math.pi * self.__radius)
