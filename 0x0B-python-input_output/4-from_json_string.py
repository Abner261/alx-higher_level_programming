#!/usr/bin/python3
""" A function that returns an object (Python data structure) """
import json
""" using the json module as we will be converting the json file to py """


def from_json_string(my_str):
    """ Return the Python data structure represented by a JSON string """
    return json.loads(my_str)
