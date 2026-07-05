#!/usr/bin/python3
"""Module that prints a dictionary's keys in alphabetical order."""


def print_sorted_dictionary(a_dictionary):
    """Print each key-value pair, sorted by key."""
    for key in sorted(a_dictionary.keys()):
        print("{}: {}".format(key, a_dictionary[key]))
