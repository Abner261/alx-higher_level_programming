#!/usr/bin/python3
""" a class MyInt that inherits from int """


class MyInt(int):
    """ a class that inherits from int"""

    def __eq__(self, value):
        """ turn the equal to to != or negator"""
        return self.real != value

    def __ne__(self, value):
        """ turn the not equal to equal"""
        return self.real == value
