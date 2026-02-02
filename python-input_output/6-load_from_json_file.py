#!/usr/bin/python3
"""6-load_from_json_file.py Defines load object from file in JSON"""


def load_from_json_file(filename):
    """Loads a Python object from a file in JSON format.

    Args:
            filename (str): The name of the file to load from.
    """
    import json

    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
