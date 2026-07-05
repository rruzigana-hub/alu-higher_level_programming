#!/usr/bin/python3
"""Module that checks divisibility by 2 for each item in a list."""


def divisible_by_2(my_list=[]):
    """Return a list of booleans indicating divisibility by 2."""
    result = []
    for num in my_list:
        result.append(num % 2 == 0)
    return result
