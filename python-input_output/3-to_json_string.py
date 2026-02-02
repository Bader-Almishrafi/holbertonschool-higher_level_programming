#!/usr/bin/python3
"""3-to_json_string.py Defines a string-to-JSON function."""


def to_json_string(my_obj):
    """Converts a Python object to a JSON string.

    Args:
                    my_obj (any): The Python object to convert.

    Returns:
                    str: The JSON string representation of the object.
    """
    import json

    return json.dumps(my_obj)
