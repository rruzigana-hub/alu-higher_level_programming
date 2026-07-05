#!/usr/bin/python3
"""Module that prints all integers of a list in reverse order."""


def print_reversed_list_integer(my_list=[]):
    """Print each integer in my_list in reverse, one per line."""
    for i in my_list[::-1]:
        print("{:d}".format(i))
