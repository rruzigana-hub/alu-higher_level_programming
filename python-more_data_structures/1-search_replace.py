#!/usr/bin/python3
"""Module that replaces occurrences of an element in a new list."""


def search_replace(my_list, search, replace):
    """Return a new list with all occurrences of search replaced."""
    return [replace if item == search else item for item in my_list]
