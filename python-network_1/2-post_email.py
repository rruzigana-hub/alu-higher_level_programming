#!/usr/bin/python3
"""Module that sends a POST request with an email parameter using urllib."""
import sys
from urllib.request import urlopen
from urllib.parse import urlencode


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = urlencode({"email": email}).encode('utf-8')
    with urlopen(url, data=data) as response:
        print(response.read().decode('utf-8'))
