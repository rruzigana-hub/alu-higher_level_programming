#!/usr/bin/python3
"""Module that squares every value in a matrix."""


def square_matrix_simple(matrix=[]):
    """Return a new matrix with every value squared."""
    return [list(map(lambda x: x ** 2, row)) for row in matrix]
