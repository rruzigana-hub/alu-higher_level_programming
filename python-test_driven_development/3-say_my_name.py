#!/usr/bin/python3
"""Module that defines a function to print a full name.

Example:
    >>> say_my_name = __import__('3-say_my_name').say_my_name
    >>> say_my_name("John", "Smith")
    My name is John Smith
"""


def say_my_name(first_name, last_name=""):
    """Print 'My name is <first_name> <last_name>'.

    Args:
        first_name (str): the first name.
        last_name (str): the last name (default "").

    Raises:
        TypeError: if first_name or last_name is not a string.
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
