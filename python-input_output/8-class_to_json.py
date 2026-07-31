#!/usr/bin/python3
"""Module that defines a function to convert an object's attributes
to a serializable dictionary.
"""


def class_to_json(obj):
    """Return the dictionary description of a simple data structure
    for JSON serialization of an object.

    Args:
        obj: an instance of a class whose attributes are all
            serializable (list, dictionary, string, integer,
            boolean).

    Returns:
        dict: the dictionary representation of obj's attributes.
    """
    return obj.__dict__
