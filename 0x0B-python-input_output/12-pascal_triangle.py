#!/usr/bin/python3
""" a function that defines pascal triangle"""


def pascal_triangle(n):
    """ A function that defines a pascal triangle and returns a list
    of lists of integers representing the pascal triangle of n"""
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        tmp = [1]
        for item in range(len(tri) - 1):
            tmp.append(tri[item] + tri[item + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
