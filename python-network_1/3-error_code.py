#!/usr/bin/python3
"""Module that fetches a URL and handles HTTPError exceptions."""
import sys
from urllib.request import urlopen
from urllib.error import HTTPError


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
