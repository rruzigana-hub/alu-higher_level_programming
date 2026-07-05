#!/usr/bin/python3
"""Module that replaces an element in a list at a given index."""


def replace_in_list(my_list, idx, element):
    """Replace my_list[idx] with element and return my_list."""
    if idx < 0:
        return my_list
    if idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list
