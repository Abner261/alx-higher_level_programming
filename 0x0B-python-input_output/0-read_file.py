#!/usr/bin/python3
""" A function that reads a text file UTF-8 and prints to standard out"""


def read_file(filename=""):
    """  The function defination """
    with open(filename, mode='r', encoding='utf-8') as a_file:
        print(a_file.read(), end='')
