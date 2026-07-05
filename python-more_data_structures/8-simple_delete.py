#!/usr/bin/python3
"""Module that deletes a key from a dictionary if it exists."""


def simple_delete(a_dictionary, key=""):
    """Delete key from a_dictionary if present, and return it."""
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
