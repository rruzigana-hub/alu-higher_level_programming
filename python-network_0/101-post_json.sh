#!/bin/bash
# Sends a POST request with JSON data read from a file
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
