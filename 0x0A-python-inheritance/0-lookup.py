#!/usr/bin/python3
""" A function that returns the list of available attributes
and methods of an object"""


def lookup(obj):
    """ The function that takes object as an argument"""
    return dir(obj)
