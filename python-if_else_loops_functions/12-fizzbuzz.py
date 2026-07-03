#!/usr/bin/python3
"""Module that prints numbers 1 to 100, replacing multiples with words."""


def fizzbuzz():
    """Print 1-100, Fizz for x3, Buzz for x5, FizzBuzz for x15."""
    for i in range(1, 101):
        if i % 15 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print("{:d}".format(i), end=" ")
