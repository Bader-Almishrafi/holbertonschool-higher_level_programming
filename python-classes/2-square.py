#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """
     Docstring for Square
     """

    def __init__(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
