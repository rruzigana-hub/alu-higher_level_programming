#!/usr/bin/python3
"""Module that prints and returns the last digit of a number."""


def print_last_digit(number):
    """Print the last digit of number and return its value."""
    last_digit = abs(number) % 10
    print("{:d}".format(last_digit), end="")
    return last_digit
