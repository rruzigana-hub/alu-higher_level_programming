#!/usr/bin/python3
"""Module that defines a class BaseGeometry with an area method."""


class BaseGeometry:
    """Base class for geometry-related classes."""

    def area(self):
        """Raise an Exception since area is not implemented."""
        raise Exception("area() is not implemented")
