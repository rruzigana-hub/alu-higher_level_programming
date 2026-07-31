#!/usr/bin/python3
"""Module that defines a function to add a new attribute to an
object, if possible.
"""


def add_attribute(obj, attr, value):
    """Add a new attribute to obj, if it's possible.

    Args:
        obj: the object to add the attribute to.
        attr (str): the name of the attribute.
        value: the value to assign to the attribute.

    Raises:
        TypeError: if obj can't have new attributes.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
