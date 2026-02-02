#!/usr/bin/python3
"""0-read_file.py Defines a text file-reading function."""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout.

    Args:
            filename (str): The name of the file to read.
    """
    with open(filename, encoding="utf-8") as r:
        print(r.read(), end="")
