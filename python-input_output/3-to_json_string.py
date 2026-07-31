#!/usr/bin/python3
"""Module that defines a function to convert an object to its JSON
string representation.
"""
import json


def to_json_string(my_obj):
    """Return the JSON representation of an object (string).

    Args:
        my_obj: the object to serialize.

    Returns:
        str: the JSON string representation of my_obj.
    """
    return json.dumps(my_obj)
