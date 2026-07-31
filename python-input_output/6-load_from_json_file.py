#!/usr/bin/python3
"""Module that defines a function to load an object from a JSON
file.
"""
import json


def load_from_json_file(filename):
    """Create an Object from a "JSON file".

    Args:
        filename (str): the name of the file to read from.

    Returns:
        the Python object represented by the JSON content of the
        file.
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
