#!/usr/bin/python3
""" an new class based on 6-base_geometry.py """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ a class that inherits from Base Geometry"""
    def __init__(self, width, height):
        """ instantation with width and height  """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """ Return the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """ return thr print() and str() rep of a rectange """
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
