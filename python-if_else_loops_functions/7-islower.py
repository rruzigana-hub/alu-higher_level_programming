#!/usr/bin/python3
"""Module that checks if a character is lowercase."""


def islower(c):
    """Return True if c is a lowercase letter, False otherwise."""
    return ord(c) >= 97 and ord(c) <= 122
