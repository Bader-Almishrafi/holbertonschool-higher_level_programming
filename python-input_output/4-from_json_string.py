#!/usr/bin/python3
"""4-from_json_string.py Defines a JSON-to-object function."""


def from_json_string(my_str):
    """Converts a JSON string to a Python object.

    Args:
      my_str (str): The JSON string to convert.
    """
    import json

    return json.loads(my_str)
