#!/usr/bin/python3
""" an new class based on 6-base_geometry.py """


class BaseGeometry:
    """ a defined class which is ment to be a base class """
    def area(self):
        """ a public instance method that raises an exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ a public instance method that validates value """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
