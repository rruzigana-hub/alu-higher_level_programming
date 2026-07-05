#!/usr/bin/python3
"""Module that returns a copy of a list with one element replaced."""


def new_in_list(my_list, idx, element):
    """Return a copy of my_list with element at idx replaced."""
    new_list = my_list[:]
    if idx < 0:
        return new_list
    if idx >= len(new_list):
        return new_list
    new_list[idx] = element
    return new_list
