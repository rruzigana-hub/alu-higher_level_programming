#!/usr/bin/python3
"""Module that defines a class Square, based on Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square, inheriting from Rectangle."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): the size of the square (used as width and
                height of the underlying rectangle).

        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is not greater than 0.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """Return the string representation of the square."""
        return "[Square] {}/{}".format(self._Rectangle__width,
                                        self._Rectangle__height)
