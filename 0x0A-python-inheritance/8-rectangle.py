#!/usr/bin/python3
""" an new class based on 6-base_geometry.py """
BaseGeometry = __import__('7-base_geometry').BaseGeometry
""" the BaseGeometry imported"""


class Rectangle(BaseGeometry):
    """ a class that inherits from Base Geometry"""
    def __init__(self, width, height):
        """ instantation with width and height  """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
