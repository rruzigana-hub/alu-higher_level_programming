#!/usr/bin/python3
"""Module with a function matching given bytecode behavior."""


def magic_calculation(a, b):
    """Perform calculation matching decoded bytecode logic."""
    from magic_calculation_102 import add, sub

    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return c
    return sub(a, b)
