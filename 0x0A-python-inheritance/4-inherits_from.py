#!/usr/bin/python3
""" A function that returns true if the obj is an istance"""


def inherits_from(obj, a_class):
    """ return true if obj is from class """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return (True)
    return (False)
