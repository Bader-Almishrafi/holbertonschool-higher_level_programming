#!/usr/bin/python3
"""BaseGeometry class."""


class BaseGeometry:
    """BaseGeometry."""

    def __init__(self, *args):
        if args:
            raise TypeError("object() takes no parameters")

    def area(self):
        """Area method not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate integer."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
