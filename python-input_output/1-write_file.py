#!/usr/bin/python3
"""1-write_file.py Defines a file-writing function."""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) and
    returns the number of characters written.

    Args:
                    filename (str): The name of the file to write to.
                    text (str): The string to write to the file."""
    with open(filename, "w", encoding="utf-8") as w:
        return w.write(text)
