#!/usr/bin/python3
"""Module that returns length and first character of a string."""


def multiple_returns(sentence):
    """Return a tuple: (length of sentence, first character or None)."""
    if len(sentence) == 0:
        return (len(sentence), None)
    return (len(sentence), sentence[0])
