#!/bin/bash
# Sends a GET request with the required custom header and displays the body
curl -s -H "X-School-User-Id: 98" -H "X-HolbertonSchool-User-Id: 98" "$1"
