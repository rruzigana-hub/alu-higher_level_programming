#!/usr/bin/python3
"""Module that finds elements present in only one of two sets."""


def only_diff_elements(set_1, set_2):
    """Return a set of elements present in only one of the sets."""
    return set_1 ^ set_2
