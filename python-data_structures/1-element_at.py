#!/usr/bin/python3
"""Module that safely retrieves an element from a list by index."""


def element_at(my_list, idx):
    """Return my_list[idx], or None if idx is negative or out of range."""
    if idx < 0:
        return None
    if idx >= len(my_list):
        return None
    return my_list[idx]
