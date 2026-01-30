#!/usr/bin/python3
"""Check inherited instance only."""


def inherits_from(obj, a_class):
    """Return True if obj inherits from a_class but is not exactly it."""
    return isinstance(obj, a_class) and type(obj) is not a_class
