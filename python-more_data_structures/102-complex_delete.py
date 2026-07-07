#!/usr/bin/python3
"""Module that deletes all keys matching a given value in a dictionary."""


def complex_delete(a_dictionary, value):
    """Delete every key in a_dictionary whose value matches value."""
    keys_to_delete = [
        key for key in a_dictionary if a_dictionary[key] == value
    ]
    for key in keys_to_delete:
        del a_dictionary[key]
    return a_dictionary
