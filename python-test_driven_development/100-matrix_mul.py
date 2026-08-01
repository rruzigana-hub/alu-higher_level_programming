#!/usr/bin/python3
"""Module that defines a function to multiply two matrices.

Example:
    >>> matrix_mul = __import__('100-matrix_mul').matrix_mul
    >>> matrix_mul([[1, 2]], [[3], [4]])
    [[11]]
"""


def matrix_mul(m_a, m_b):
    """Multiply two matrices together.

    Args:
        m_a: the first matrix, a list of lists of integers/floats.
        m_b: the second matrix, a list of lists of integers/floats.

    Returns:
        list: the resulting matrix from multiplying m_a by m_b.

    Raises:
        TypeError: if m_a/m_b are not valid list-of-lists matrices,
            contain non-numeric elements, or have inconsistent rows.
        ValueError: if m_a/m_b are empty, or can't be multiplied.
    """
    for name, matrix in (("m_a", m_a), ("m_b", m_b)):
        if not isinstance(matrix, list):
            raise TypeError("{} must be a list".format(name))
        if not all(isinstance(row, list) for row in matrix):
            raise TypeError("{} must be a list of lists".format(name))
        if matrix == [] or matrix == [[]]:
            raise ValueError("{} can't be empty".format(name))
        for row in matrix:
            for item in row:
                if type(item) not in (int, float):
                    raise TypeError(
                        "{} should contain only integers or floats"
                        .format(name))
        if len(set(len(row) for row in matrix)) != 1:
            raise TypeError(
                "each row of {} must be of the same size".format(name))

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = []
    for row in m_a:
        new_row = []
        for col in range(len(m_b[0])):
            total = 0
            for i in range(len(m_b)):
                total += row[i] * m_b[i][col]
            new_row.append(total)
        result.append(new_row)
    return result
