#!/usr/bin/python3
"""Module that defines a Student class with an optional attribute
filter for JSON serialization.
"""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name (str): the student's first name.
            last_name (str): the student's last name.
            age (int): the student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of a Student
        instance, optionally filtered by attribute name.

        Args:
            attrs (list): optional list of attribute names to
                include. If None, all attributes are included.

        Returns:
            dict: the dictionary representation of the instance's
            attributes.
        """
        if isinstance(attrs, list) and all(
                isinstance(attr, str) for attr in attrs):
            return {key: value for key, value in self.__dict__.items()
                    if key in attrs}
        return self.__dict__
