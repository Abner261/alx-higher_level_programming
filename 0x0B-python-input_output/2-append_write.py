#!/usr/bin/python3
"""A function that appends a string at the end of a text file (UTF8)"""

def append_write(filename="", text=""):
    """Open the file in append mode ('a') using 'utf-8' encoding"""
    with open(filename, mode='a', encoding='utf-8') as a_file:
        return a_file.write(text)
