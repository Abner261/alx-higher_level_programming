#!/usr/bin/python3
""" a function that returns true if the obj is specified class"""


def is_same_class(obj, a_class):
    """ checks if the object is the same class"""
    if type(obj) is a_class:
        return (True)
    return (False)
