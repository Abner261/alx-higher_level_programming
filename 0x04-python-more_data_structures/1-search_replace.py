#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = [replace if n == search else n for n in my_list]
    return (new_list)
"""
[1]search_replace: A function that replaces all occurrences
of an element by another in a new list
[2]Prototype: def search_replace(my_list, search, replace):
[3]my_list: This is the initial list
[4]search: This is the element to replace in the list
[5]replace: This is the new element
"""
