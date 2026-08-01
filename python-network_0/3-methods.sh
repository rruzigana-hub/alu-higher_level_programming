#!/bin/bash
# Displays all HTTP methods the server accepts for a URL
curl -s -X OPTIONS -D - -o /dev/null "$1" | grep -i "^Allow:" | cut -d' ' -f2- | tr -d '\r'
