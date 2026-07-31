#!/usr/bin/python3
"""Module that defines a function to write a string to a text
file.
"""


def write_file(filename="", text=""):
    """Write a string to a text file (UTF8) and return the number
    of characters written.

    Args:
        filename (str): the name of the file to write to.
        text (str): the text to write into the file.

    Returns:
        int: the number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
