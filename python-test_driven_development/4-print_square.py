#!/usr/bin/python3
"""Module that defines a function to print a square of # characters.

Example:
    >>> print_square = __import__('4-print_square').print_square
    >>> print_square(2)
    ##
    ##
"""


def print_square(size):
    """Print a square with the character #.

    Args:
        size (int): the size length of the square.

    Raises:
        TypeError: if size is not an integer.
        ValueError: if size is less than 0.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
