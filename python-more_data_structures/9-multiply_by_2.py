#!/usr/bin/python3
"""Module that returns a new dictionary with values multiplied by 2."""


def multiply_by_2(a_dictionary):
    """Return a new dictionary with every value doubled."""
    return {key: value * 2 for key, value in a_dictionary.items()}
