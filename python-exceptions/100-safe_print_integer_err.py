#!/usr/bin/python3
"""Module that safely prints a value as an integer, logging errors."""
from sys import stderr


def safe_print_integer_err(value):
    """Print value as integer; on failure, print error to stderr."""
    try:
        print("{:d}".format(value))
        return True
    except Exception as e:
        print("Exception: {}".format(e), file=stderr)
        return False
