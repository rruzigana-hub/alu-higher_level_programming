#!/usr/bin/python3
"""Module that displays the X-Request-Id header value for a URL."""
import sys
from urllib.request import urlopen


if __name__ == "__main__":
    with urlopen(sys.argv[1]) as response:
        print(response.getheader("X-Request-Id"))
