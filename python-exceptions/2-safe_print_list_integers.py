#!/usr/bin/python3
"""Module that prints only integers from the first x elements of a list."""


def safe_print_list_integers(my_list=[], x=0):
    """Print only integer elements among the first x, return count."""
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            continue
    print()
    return count
