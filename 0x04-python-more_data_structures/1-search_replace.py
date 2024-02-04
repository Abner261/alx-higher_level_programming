#!/usr/bin/python3

"""
search_replace: A function that replaces all occurrences
of an element by another in a new list
Prototype: def search_replace(my_list, search, replace):
my_list: This is the initial list
search: This is the element to replace in the list
replace: This is the new element
"""

def search_replace(my_list, search, replace):
    return [replace if search == n else n for n in my_list]
