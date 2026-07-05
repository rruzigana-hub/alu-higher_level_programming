#!/usr/bin/python3
"""Module that safely divides two integers, printing debug info."""


def safe_print_division(a, b):
    """Divide a by b, print result in finally, return value or None."""
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
