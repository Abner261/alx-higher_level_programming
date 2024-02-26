#!/usr/bin/python3
"""

writes an Object to a text file using a JSON representation

Args:
my_obj: object to write
filename: textfile to be written into

"""
import json
"""This module will be used as json is needed"""


def save_to_json_file(my_obj, filename):
    """Open the file in write mode ('w') using 'utf-8' encoding"""
    with open(filename, mode='w', encoding='utf-8') as file:
        return file.write(json.dumps(my_obj))
