#!/usr/bin/python3
"""Module with a function matching given bytecode behavior."""


def magic_calculation(a, b):
    """Perform calculation matching decoded bytecode logic."""
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            result += a ** b / i
        except Exception:
            result = b + a
            break
    return result
