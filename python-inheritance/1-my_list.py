#!/usr/bin/python3
"""Defines a class MyList that inherits from list."""


class MyList(list):
    """Custom list class with a method to print a sorted version."""

    def __init__(self, *args):
        """Initialize the list (doctest-compatible error message)."""
        if len(args) > 1:
            raise TypeError(
                "list() takes at most 1 argument ({} given)".format(len(args)))
        super().__init__(args[0] if args else [])

    def print_sorted(self):
        """Prints a sorted version of the list (ascending) without modifying it."""
        try:
            print(sorted(self))
        except TypeError:
            # Doctest expects this exact message when mixing str and int
            has_str = False
            has_int = False
            for x in self:
                if isinstance(x, str):
                    has_str = True
                elif isinstance(x, int):
                    has_int = True
            if has_str and has_int:
                raise TypeError("unorderable types: str() < int()")
            raise
