#!/usr/bin/python3
"""5-save_to_json_file.py Defines save object to file in JSON"""


def save_to_json_file(my_obj, filename):
    """Saves a Python object to a file in JSON format.

    Args:
        my_obj (any): The Python object to save.
        filename (str): The name of the file to save to.
    """
    import json

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
