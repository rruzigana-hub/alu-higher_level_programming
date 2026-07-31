#!/usr/bin/python3
"""Module that defines a function to save an object to a JSON file."""
import json


def save_to_json_file(my_obj, filename):
    """Write an Object to a text file, using a JSON representation.

    Args:
        my_obj: the object to serialize.
        filename (str): the name of the file to write to.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
