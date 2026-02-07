#!/usr/bin/python3
"""
8-class_to_json.py Returns the dictionary description of an object
for JSON serialization.
"""


def class_to_json(obj):
    """Return the dictionary representation of an object"""
    return obj.__dict__
