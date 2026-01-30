#!/usr/bin/python3
"""Defines a class MyList that inherits from list."""


class MyList(list):
    """Custom list class with a method to print a sorted version."""

    def __init__(self, *args):
        """Initialize the list."""
        if len(args) > 1:
            raise TypeError(
                "list() takes at most 1 argument ({} given)".format(len(args))
            )
        if args:
            super().__init__(args[0])
        else:
            super().__init__()

    def print_sorted(self):
        """Print the list sorted in ascending order."""
        try:
            print(sorted(self))
        except TypeError:
            has_str = False
            has_int = False

            for item in self:
                if isinstance(item, str):
                    has_str = True
                elif isinstance(item, int):
                    has_int = True

            if has_str and has_int:
                raise TypeError(
                    "unorderable types: str() < int()"
                ) from None
            raise
