#!/usr/bin/python3
"""Defines a BaseGeometry class with integer validation."""


class BaseGeometry:
    """BaseGeometry class."""

    def __init__(self, *args, **kwargs):
        """Initialize BaseGeometry.

        Doctest expects a specific TypeError message when parameters are passed.
        """
        if args or kwargs:
            raise TypeError("object() takes no parameters")

    def area(self):
        """Raise an exception indicating area is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a positive integer."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
