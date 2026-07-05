#!/usr/bin/python3
"""Module that removes all c and C characters from a string."""


def no_c(my_string):
    """Return my_string with all c and C characters removed."""
    result = ""
    for char in my_string:
        if char != "c" and char != "C":
            result += char
    return result
