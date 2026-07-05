#!/usr/bin/python3
"""Module that deletes an item at a specific index in a list."""


def delete_at(my_list=[], idx=0):
    """Delete the item at idx in my_list and return the list."""
    if idx < 0:
        return my_list
    if idx >= len(my_list):
        return my_list
    del my_list[idx]
    return my_list
