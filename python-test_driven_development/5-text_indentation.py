#!/usr/bin/python3
"""Module that defines a function to print text with indentation.

Example:
    >>> text_indentation = __import__('5-text_indentation').text_indentation
    >>> text_indentation("Hello. World.")
    Hello.
    <BLANKLINE>
    World.
    <BLANKLINE>
"""


def text_indentation(text):
    """Print a text with 2 new lines after each ., ? and : character.

    Args:
        text (str): the text to print.

    Raises:
        TypeError: if text is not a string.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    stripped = text.strip()
    result = ""
    i = 0
    while i < len(stripped):
        char = stripped[i]
        result += char
        if char in ".?:":
            result += "\n\n"
            i += 1
            while i < len(stripped) and stripped[i] == " ":
                i += 1
            continue
        i += 1
    print(result.strip())
