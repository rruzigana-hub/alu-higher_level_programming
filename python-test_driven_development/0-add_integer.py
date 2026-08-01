#!/usr/bin/python3
"""Module that defines a function to add two integers.

Example:
    >>> add_integer = __import__('0-add_integer').add_integer
    >>> add_integer(1, 2)
    3
"""


def add_integer(a, b=98):
    """Add two integers or floats (casted to integers) together.

    Args:
        a: the first number, must be an integer or float.
        b: the second number, must be an integer or float (default 98).

    Returns:
        int: the sum of a and b.

    Raises:
        TypeError: if a or b is not an integer or float.
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
