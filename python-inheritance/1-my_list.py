#!/usr/bin/python3
"""Defines a class MyList that inherits from list."""


class MyList(list):
    """Custom list class with a method to print a sorted version."""

    def __init__(self, *args):
        """Initialize the list (doctest-compatible error message)."""
        if len(args) > 1:
            raise TypeError(
                "list() takes at most 1 argument ({} given)".format(len(args))
            )
        super().__init__(args[0] if args else [])

    def print_sorted(self):
        """Prints a sorted version of the list (ascending)."""
        try:
            print(sorted(self))
        except TypeError:
            first = None
            second = None

            for x in self:
                t = type(x).__name__
                if first is None:
                    first = t
                elif t != first:
                    second = t
                    break

            if first and second:
                raise TypeError(
                    "unorderable types: {}() < {}()".format(first, second)
                )
            raise
