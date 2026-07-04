#!/usr/bin/python3
"""Program that prints names defined in the hidden_4 module."""
import hidden_4

if __name__ == "__main__":
    names = dir(hidden_4)
    for name in names:
        if not name.startswith("__"):
            print(name)
