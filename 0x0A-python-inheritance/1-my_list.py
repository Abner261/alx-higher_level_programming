#!/usr/bin/python3
""" A class mylist that inherits a base list list"""


class MyList(list):
    """ the class mylist that takes the base class as an argument"""
    def print_sorted(self):
        """ a function defination for my list to print sorted self"""
        print(sorted(self))
