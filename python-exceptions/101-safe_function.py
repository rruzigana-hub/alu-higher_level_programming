#!/usr/bin/python3
"""Module that safely executes any function with given arguments."""
from sys import stderr


def safe_function(fct, *args):
    """Call fct with args; return result or None on error."""
    try:
        return fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=stderr)
        return None
