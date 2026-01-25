#!/usr/bin/python3
"""
0-add_integer module
Defines a function that adds two integers.
"""


def add_integer(a, b=98):
    """
    Add two integers.

    Args:
        a (int or float): first number
        b (int or float): second number (default is 98)

    Raises:
        TypeError: if a or b is not an integer or float

    Returns:
        int: the sum of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
