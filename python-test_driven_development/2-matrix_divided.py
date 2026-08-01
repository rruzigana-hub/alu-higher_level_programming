#!/usr/bin/python3
"""Module that defines a function to divide all elements of a matrix.

Example:
    >>> matrix_divided = __import__('2-matrix_divided').matrix_divided
    >>> matrix_divided([[1, 2], [3, 4]], 2)
    [[0.5, 1.0], [1.5, 2.0]]
"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by div, rounded to 2 decimals.

    Args:
        matrix: a list of lists of integers or floats.
        div: the divisor, an integer or float.

    Returns:
        list: a new matrix with all elements divided by div.

    Raises:
        TypeError: if matrix is not a valid matrix, rows differ in
            size, or div is not a number.
        ZeroDivisionError: if div is 0.
    """
    if (not isinstance(matrix, list) or len(matrix) == 0 or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) of "
                         "integers/floats")
    for row in matrix:
        for item in row:
            if type(item) not in (int, float):
                raise TypeError("matrix must be a matrix (list of "
                                 "lists) of integers/floats")
    if len(set(len(row) for row in matrix)) != 1:
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(item / div, 2) for item in row] for row in matrix]
