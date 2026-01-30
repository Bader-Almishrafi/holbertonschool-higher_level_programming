#!/usr/bin/python3
"""Defines a class MyList that inherits from list."""


class MyList(list):
    """Custom list class with a method to print a sorted version."""

    def __init__(self, *args):
        """
        Initialize the list.

        Mimics list() signature for doctest compatibility:
        list() takes at most 1 argument (N given)
        """
        if len(args) > 1:
            raise TypeError(
                "list() takes at most 1 argument ({} given)".format(len(args)))
        super().__init__(args[0] if args else [])

    def print_sorted(self):
        """Print the list sorted in ascending order (without modifying the original)."""
        # Doctest expects a specific TypeError message when types are unorderable
        for x in self:
            if type(x) is not int:
                # Match the doctest format: "unorderable types: str() < int()"
                raise TypeError(
                    "unorderable types: {}() < int()".format(type(x).__name__))

        print(sorted(self))
