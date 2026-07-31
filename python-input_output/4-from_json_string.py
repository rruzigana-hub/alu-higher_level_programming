#!/usr/bin/python3
"""Module that defines a function to convert a JSON string to a
Python data structure.
"""
import json


def from_json_string(my_str):
    """Return an object (Python data structure) represented by a
    JSON string.

    Args:
        my_str (str): the JSON string to deserialize.

    Returns:
        the Python object represented by my_str.
    """
    return json.loads(my_str)
