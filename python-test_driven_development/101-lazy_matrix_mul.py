#!/usr/bin/python3
"""Module that defines a function to multiply two matrices using NumPy.

Example:
    >>> lazy_matrix_mul = __import__('101-lazy_matrix_mul').lazy_matrix_mul
    >>> lazy_matrix_mul([[1, 2]], [[3], [4]])
    array([[11]])
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiply two matrices together using NumPy.

    Args:
        m_a: the first matrix.
        m_b: the second matrix.

    Returns:
        numpy.ndarray: the resulting matrix.
    """
    return np.matmul(m_a, m_b)
