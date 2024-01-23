#!/usr/bin/python3
"""Square Module"""


class Square:
    """Define a Class named Square"""

    def area(self):
    """Area of square

    Return:
        the size squared.
    """
        return self.__size ** 2

    def __init__(self, size=0):
    """Constructor:

    Args:
        size: len of a side of the square.
    Raise:
        TypeError: if size is not int.
        ValueError: if size if less than 0.
    """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    @property
    def size(self):
        """Property for len of a side of the square

        Raise:
            TypeError: if size is not int.
            ValueError: if size if less than 0.
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value
