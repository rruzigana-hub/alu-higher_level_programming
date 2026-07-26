#!/usr/bin/python3
"""Module that checks if an object is exactly an instance of a class."""


def is_same_class(obj, a_class):
    """Return True if obj's exact type is a_class, False otherwise."""
    return type(obj) is a_class
