#!/usr/bin/python3
"""2-append_write.py Defines a file-appending function."""


def append_write(filename="", text=""):
    """Appends a string to the end of a text file (UTF8)
    and returns the number of characters added.

    Args:
                    filename (str): The name of the file to append to.
                    text (str): The string to append to the file.
    """
    with open(filename, "a", encoding="utf-8") as a:
        return a.write(text)
