#!/usr/bin/python3
"""Module that finds the key with the highest value in a dictionary."""


def best_score(a_dictionary):
    """Return the key with the highest value, or None if empty/None."""
    if not a_dictionary:
        return None
    best_key = None
    best_value = None
    for key, value in a_dictionary.items():
        if best_value is None or value > best_value:
            best_key = key
            best_value = value
    return best_key
