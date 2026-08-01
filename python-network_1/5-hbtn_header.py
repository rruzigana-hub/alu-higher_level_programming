#!/usr/bin/python3
"""Module that displays the X-Request-Id header value using requests."""
import sys
import requests


if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    print(response.headers.get("X-Request-Id"))
