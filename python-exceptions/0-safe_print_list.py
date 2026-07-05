#!/usr/bin/python3
"""Module that safely prints x elements of a list."""


def safe_print_list(my_list=[], x=0):
    """Print up to x elements of my_list, return count printed."""
    count = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            count += 1
        except IndexError:
            break
    print()
    return count
