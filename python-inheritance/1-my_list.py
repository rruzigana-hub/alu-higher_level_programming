#!/usr/bin/python3
"""Module that defines MyList, a list subclass with sorted printing."""


class MyList(list):
    """Represents a list that can print itself sorted."""

    def print_sorted(self):
        """Print the list in ascending sorted order."""
        print(sorted(self))
