#!/usr/bin/python3
"""Defines file-writing function."""


def write_file(filename="", text=""):
    """A function that writes a string to a text file (UTF8)

    Args:
        filename (str): Name of the file to write
        text (str): The text to write to the file
    Returns:
        Number of characters written
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
