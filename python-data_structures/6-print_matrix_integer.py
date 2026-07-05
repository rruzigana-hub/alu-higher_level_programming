#!/usr/bin/python3
"""Module that prints a matrix of integers."""


def print_matrix_integer(matrix=[[]]):
    """Print each row of matrix, space-separated, one row per line."""
    for row in matrix:
        line = ""
        for i in range(len(row)):
            if i > 0:
                line += " "
            line += "{:d}".format(row[i])
        print(line)
