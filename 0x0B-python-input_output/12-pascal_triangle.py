#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n.

    Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        trianle = triangles[-1]
        buf = [1]
        for i in range(len(triangle) - 1):
            buf.append(triangle[i] + triangle[i + 1])
        buf.append(1)
        triangles.append(buf)
    return triangles
