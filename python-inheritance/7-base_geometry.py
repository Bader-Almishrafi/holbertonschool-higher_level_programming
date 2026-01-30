#!/usr/bin/python3
"""BaseGeometry class with validation."""


class BaseGeometry:
    """BaseGeometry class."""

    def __init__(self, *args, **kwargs):
        if args or kwargs:
            raise TypeError("object() takes no parameters")

    def area(self):
        """Raise an exception for unimplemented area."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a positive integer value."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
