#!/usr/bin/python3

"""A function that creates an Object from a JSON file"""


def load_from_json_file(filename):
    """
    Function to load object from json file.
    Args:
        filename
    Return:
        object created from the file.
    """
    import json

    with open(filename) as obj_file:
        new_file = json.load(obj_file)
        return new_file
