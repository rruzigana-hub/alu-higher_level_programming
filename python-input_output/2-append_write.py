#!/usr/bin/python3
"""Module that defines a function to append a string to a text
file.
"""


def append_write(filename="", text=""):
    """Append a string at the end of a text file (UTF8) and return
    the number of characters added.

    Args:
        filename (str): the name of the file to append to.
        text (str): the text to append to the file.

    Returns:
        int: the number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
