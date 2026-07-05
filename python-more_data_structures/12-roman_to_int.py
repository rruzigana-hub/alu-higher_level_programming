#!/usr/bin/python3
"""Module that converts a Roman numeral to an integer."""


def roman_to_int(roman_string):
    """Convert roman_string to its integer value."""
    if type(roman_string) is not str or roman_string is None:
        return 0

    values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    total = 0
    for i in range(len(roman_string)):
        current = values.get(roman_string[i], 0)
        if i + 1 < len(roman_string):
            next_value = values.get(roman_string[i + 1], 0)
            if current < next_value:
                total -= current
            else:
                total += current
        else:
            total += current

    return total
