#!/usr/bin/python3
"""Module that defines a class MyInt, inheriting from int, with
inverted == and != operators.
"""


class MyInt(int):
    """Rebel integer class where == and != are inverted."""

    def __eq__(self, other):
        """Return the opposite of the normal equality comparison."""
        return int(self) != int(other)

    def __ne__(self, other):
        """Return the opposite of the normal inequality comparison."""
        return int(self) == int(other)
